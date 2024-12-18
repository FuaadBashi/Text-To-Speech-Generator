from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root, width=400 , height= 300)
canvas.pack()

def text_to_speech():
    text = entry.get()
    output = gTTS(text=text, lang='en', slow=False)
    output.save("output.mp3")
    os.system("afply output.mp3")


entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button = Button(text="START", command=text_to_speech)
canvas.create_window(200, 220, window=button)

root.mainloop()

