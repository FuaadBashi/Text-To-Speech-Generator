# Text-to-Speech Desktop App

A small Python/Tkinter application that converts entered English text to an MP3 using gTTS and plays it locally.

## Run locally

Requires Python 3 with Tkinter, internet access for gTTS, and **macOS** for the current `afplay` playback command.

```bash
git clone https://github.com/FuaadBashi/Text-To-Speech-Generator.git
cd Text-To-Speech-Generator
python3 -m venv .venv
source .venv/bin/activate
python -m pip install gTTS
python main.py
```

## Try it

1. Enter a short sentence.
2. Click **START** to generate and play `output.mp3`.
3. Click **CLEAR** to reset the input or **EXIT** to close the window.

## Code to explore

[main.py](main.py) contains the GUI and conversion callback. Text is sent to the external gTTS service, and each conversion overwrites `output.mp3` in the working directory. Conversion and playback run synchronously in the UI callback; background execution is a useful next improvement.
