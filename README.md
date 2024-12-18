# Text-To-Speech-Generator
A simple Python-based text-to-speech application using gtts and tkinter. Enter text into a GUI input field, click START, and hear the text converted to speech. Audio is saved as output.mp3 and played using your system's media player. Easy to use, lightweight, and customizable for future enhancements.

# Text-to-Speech App

This repository contains a simple text-to-speech application built using Python's `gtts` (Google Text-to-Speech) library and the `tkinter` GUI toolkit. Users can input text, convert it to speech, and play the audio directly.

## Features
- Convert user-entered text into speech using Google TTS.
- Save the speech as an audio file (`output.mp3`).
- Simple graphical user interface (GUI) with input and button controls.

## Requirements
- Python 3.7 or higher
- gTTS library
- tkinter (comes pre-installed with Python)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-to-speech-app
   ```
2. Navigate to the project folder:
   ```bash
   cd text-to-speech-app
   ```
3. Install the required library:
   ```bash
   pip install gtts
   ```

## How to Run
1. Open a terminal and run the following command:
   ```bash
   python main.py
   ```
2. A window will appear where you can enter text.
3. Click the **START** button to convert the text to speech.

## Code Overview
- **gTTS**: Used to convert text to speech and save it as `output.mp3`.
- **os.system**: Plays the saved audio file using a system media player.
- **tkinter**: Handles the graphical user interface.

### Main Components:
- **Entry Widget**: Input text field for users.
- **Button**: Trigger the text-to-speech conversion.
- **Canvas**: GUI layout management.

## Example
1. Enter text into the input field.
2. Click **START**.
3. The text will be converted into speech and played as an audio file.

## Future Enhancements
- Add language selection support.
- Integrate a custom media player for better audio playback.
- Add support for saving multiple audio files.

## License
This project is licensed under the MIT License.
