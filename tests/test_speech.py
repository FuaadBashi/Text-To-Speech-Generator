from pathlib import Path

import pytest

from speech import SpeechError, languages, play_command, synthesize


class FakeEngine:
    """Stands in for gTTS so tests never touch the network."""

    calls = []

    def __init__(self, text, lang, slow):
        FakeEngine.calls.append((text, lang, slow))

    def save(self, path):
        Path(path).write_bytes(b"ID3fake")


class OfflineEngine:
    def __init__(self, **kwargs):
        pass

    def save(self, path):
        raise ConnectionError("no network")


def test_text_is_trimmed_and_saved_as_audio(tmp_path):
    FakeEngine.calls.clear()
    out = synthesize("  Hello there  ", "en", tmp_path / "out.mp3", engine=FakeEngine)

    assert out.read_bytes() == b"ID3fake"
    assert FakeEngine.calls == [("Hello there", "en", False)]


def test_blank_text_is_rejected_before_any_network_call(tmp_path):
    FakeEngine.calls.clear()
    with pytest.raises(SpeechError, match="enter some text"):
        synthesize("   \n", "en", tmp_path / "out.mp3", engine=FakeEngine)
    assert FakeEngine.calls == []


def test_an_unknown_language_is_rejected(tmp_path):
    with pytest.raises(SpeechError, match="Unsupported language"):
        synthesize("Hi", "xx", tmp_path / "out.mp3", engine=FakeEngine)


def test_a_network_failure_becomes_a_readable_error(tmp_path):
    with pytest.raises(SpeechError, match="Couldn't reach"):
        synthesize("Hi", "en", tmp_path / "out.mp3", engine=OfflineEngine)


def test_languages_include_english_and_are_sorted_by_name():
    langs = languages()

    assert langs["en"] == "English"
    assert list(langs.values()) == sorted(langs.values())


def test_macos_uses_afplay_and_windows_uses_the_file_handler():
    assert play_command(Path("a.mp3"), "Darwin") == ["afplay", "a.mp3"]
    assert play_command(Path("a.mp3"), "Windows") is None


def test_linux_falls_back_to_the_desktop_opener(monkeypatch):
    monkeypatch.setattr("speech.shutil.which", lambda name: None)

    assert play_command(Path("a.mp3"), "Linux") == ["xdg-open", "a.mp3"]
