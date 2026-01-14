#The purpose of this script is to be changed, and turn into other scripts and tools.

from tkinter import *
import webbrowser

url = input("URL: ")
webbrowser.open(url)

window = Tk()
window.title("URL")
window.geometry("1100x300")

label = Label(
    window,
    text=("Opened: ",url),
    font=("Comic Sans MS", 60),
    fg="red"
)
label.pack()
window.mainloop()
