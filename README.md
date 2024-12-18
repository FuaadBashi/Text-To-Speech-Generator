# Text-To-Speech-Generator
A simple Python-based text-to-speech application using gtts and tkinter. Enter text into a GUI input field, click START, and hear the text converted to speech. Audio is saved as output.mp3 and played using your system's media player. Easy to use, lightweight, and customizable for future enhancements.

This is a simple **Text-to-Speech Generator** built with Python's **Tkinter** for the graphical user interface and **gTTS (Google Text-to-Speech)** for generating speech from text.  

---

## Features  
- **Convert Text to Speech**: Input text and listen to the generated speech.  
- **Clear Input**: Easily reset the text field with the "CLEAR" button.  
- **User-Friendly Interface**: Simple and clean design with intuitive controls.  
- **Cross-Platform**: Works on Windows, macOS, and Linux.  

---

## Prerequisites  
Before running the app, ensure you have the following:  

- **Python 3.8+** installed.  
- **gTTS** (Google Text-to-Speech library).  

You can install `gTTS` using:  
```bash
pip install gtts
```

---

## How to Run  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/text-to-speech-app.git
   cd text-to-speech-app
   ```

2. Run the Python script:  
   ```bash
   python3 main.py
   ```

3. Input text into the provided field, click **START**, and listen to the audio.  

4. Use the **CLEAR** button to reset the field or **EXIT** to close the app.  

---

## Code Overview  

The app is structured using:  
- **Tkinter**: For building the graphical interface.  
- **gTTS**: To convert text to speech and save it as an audio file.  
- **os**: To play the generated audio file.  

Here’s a glimpse of the main components:  

```python
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
```

---

## Notes for Different OS  

- **macOS**: Uses `afplay` to play the audio file.  
- **Windows**: Replace `os.system("afplay output.mp3")` with:  
   ```python
   os.system("start output.mp3")
   ```
- **Linux**: Use a command like `mpg123` to play the file. Ensure the package is installed:  
   ```bash
   sudo apt-get install mpg123
   ```

---

## Contributing  

Contributions are welcome!  
1. Fork the repository.  
2. Create a feature branch: `git checkout -b new-feature`.  
3. Commit changes: `git commit -m "Add new feature"`.  
4. Push to your branch: `git push origin new-feature`.  
5. Submit a Pull Request.  

---

## License  

This project is open-source and available under the [MIT License](LICENSE).  

---

### Enjoy converting text to speech effortlessly! 🚀  

Let me know if you'd like further customizations or additional sections added to the README. 😊
