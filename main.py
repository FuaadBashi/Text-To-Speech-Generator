from gtts import gTTS
import os
from tkinter import *

# Main window setup
root = Tk()
root.title("Text-to-Speech App")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Function to handle text-to-speech conversion
def text_to_speech():
    text = entry.get("1.0", "end-1c")  # Get full text from Text widget
    if text.strip():
        output = gTTS(text=text, lang='en', slow=False)
        output.save("output.mp3")
        os.system("afplay output.mp3")
        confirmation_label.config(text="Success! Audio is playing.", fg="green")
    else:
        confirmation_label.config(text="Error: Text field is empty.", fg="red")

# Function to clear the input field
def clear_text():
    entry.delete("1.0", END)
    confirmation_label.config(text="")

# UI Elements
canvas = Canvas(root, width=500, height=400, bg="#f0f0f0", highlightthickness=0)
canvas.pack()

# Title label
title_label = Label(root, text="Text-to-Speech Converter", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="black")
canvas.create_window(250, 50, window=title_label)

# Text input label
input_label = Label(root, text="Enter your text below:", font=("Helvetica", 12), bg="#f0f0f0", fg="black")
canvas.create_window(250, 100, window=input_label)

# Multi-line text entry
entry = Text(root, width=50, height=5, font=("Helvetica", 12), fg="black")
canvas.create_window(250, 160, window=entry)

# Confirmation label
confirmation_label = Label(root, text="", font=("Helvetica", 10), fg="green", bg="#f0f0f0")
canvas.create_window(250, 220, window=confirmation_label)

# START button
start_button = Button(root, text="START", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="black", width=10, command=text_to_speech)
canvas.create_window(150, 270, window=start_button)

# CLEAR button
clear_button = Button(root, text="CLEAR", font=("Helvetica", 12, "bold"), bg="#FF9800", fg="black", width=10, command=clear_text)
canvas.create_window(250, 270, window=clear_button)

# EXIT button
exit_button = Button(root, text="EXIT", font=("Helvetica", 12, "bold"), bg="#F44336", fg="black", width=10, command=root.destroy)
canvas.create_window(350, 270, window=exit_button)


root.mainloop()