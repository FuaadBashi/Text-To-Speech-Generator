"""Text-to-speech core: synthesis and playback, with no Tkinter dependency."""

from __future__ import annotations

import os
import platform
import shutil
import subprocess
from collections.abc import Callable
from pathlib import Path

from gtts import gTTS
from gtts.lang import tts_langs

# gTTS(text=..., lang=...) -> object with .save(path); injectable so tests never hit the network.
Engine = Callable[..., object]


class SpeechError(Exception):
    """Something the user should be told about, such as empty text or no network."""


def languages() -> dict[str, str]:
    """Language code -> name, sorted by name. gTTS ships this list, so no network is needed."""
    return dict(sorted(tts_langs().items(), key=lambda item: item[1]))


def synthesize(text: str, lang: str, path: Path, engine: Engine = gTTS) -> Path:
    text = text.strip()
    if not text:
        raise SpeechError("Please enter some text first.")
    if lang not in tts_langs():
        raise SpeechError(f"Unsupported language: {lang}")
    try:
        engine(text=text, lang=lang, slow=False).save(str(path))
    except Exception as e:  # gTTS raises several types for network and API failures
        raise SpeechError(f"Couldn't reach the text-to-speech service: {e}") from e
    return path


def play_command(path: Path, system: str | None = None) -> list[str] | None:
    """The command that plays an MP3 on this OS, or None to use the OS file handler.

    The original always ran macOS's afplay, so playback failed everywhere else.
    """
    system = system or platform.system()
    if system == "Darwin":
        return ["afplay", str(path)]
    if system == "Windows":
        return None
    for player in (["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet"], ["mpg123", "-q"]):
        if shutil.which(player[0]):
            return [*player, str(path)]
    return ["xdg-open", str(path)]


def play(path: Path) -> None:
    command = play_command(path)
    try:
        if command is None:
            os.startfile(path)  # type: ignore[attr-defined]  # Windows only
        else:
            # A list argument, not a shell string, so an odd file name can't run anything.
            subprocess.run(
                command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
    except (OSError, subprocess.CalledProcessError) as e:
        raise SpeechError(f"Couldn't play the audio: {e}") from e
