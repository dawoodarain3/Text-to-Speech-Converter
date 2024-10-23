import pyttsx3
import tkinter as tk

def speachconversion():
    text = entry.get()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

window = tk.Tk()
window.title("Text to Speech Converter")

label = tk.Label(window, text="Enter Text:")
label.pack()
entry = tk.Entry(window, width=50)
entry.pack()
button = tk.Button(window, text="Convert to Speech", command=speachconversion)
button.pack()

window.mainloop()