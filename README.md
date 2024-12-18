# Text-To-Speech-Generator
A simple Python-based text-to-speech application using gtts and tkinter. Enter text into a GUI input field, click START, and hear the text converted to speech. Audio is saved as output.mp3 and played using your system's media player. Easy to use, lightweight, and customizable for future enhancements.

Text-to-Speech App 🎤
This is a simple Text-to-Speech Converter built with Python's Tkinter for the graphical user interface and gTTS (Google Text-to-Speech) for generating speech from text.

Features
Convert Text to Speech: Input text and listen to the generated speech.
Clear Input: Easily reset the text field with the "CLEAR" button.
User-Friendly Interface: Simple and clean design with intuitive controls.
Cross-Platform: Works on Windows, macOS, and Linux.

Main Interface
Prerequisites
Before running the app, ensure you have the following:

Python 3.8+ installed.
gTTS (Google Text-to-Speech library).
You can install gTTS using:

bash
Copy code
pip install gtts
How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/text-to-speech-app.git
cd text-to-speech-app
Run the Python script:

bash
Copy code
python3 main.py
Input text into the provided field, click START, and listen to the audio.

Use the CLEAR button to reset the field or EXIT to close the app.

Code Overview
The app is structured using:

Tkinter: For building the graphical interface.
gTTS: To convert text to speech and save it as an audio file.
os: To play the generated audio file.
Here’s a glimpse of the main components:

python
Copy code
from gtts import gTTS
import os
from tkinter import *

# Function for Text-to-Speech
def text_to_speech():
    text = entry.get("1.0", "end-1c")
    if text.strip():
        output = gTTS(text=text, lang='en', slow=False)
        output.save("output.mp3")
        os.system("afplay output.mp3")  # Replace 'afplay' with 'start' for Windows
Notes for Different OS
macOS: Uses afplay to play the audio file.
Windows: Replace os.system("afplay output.mp3") with:
python
Copy code
os.system("start output.mp3")
Linux: Use a command like mpg123 to play the file. Ensure the package is installed:
bash
Copy code
sudo apt-get install mpg123
Contributing
Contributions are welcome!

Fork the repository.
Create a feature branch: git checkout -b new-feature.
Commit changes: git commit -m "Add new feature".
Push to your branch: git push origin new-feature.
Submit a Pull Request.
License
This project is open-source and available under the MIT License.

