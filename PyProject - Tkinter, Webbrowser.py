from tkinter import *
import webbrowser

url = input("Which URL would you like to surf to? ")

webbrowser.open(url)

window = Tk()
window.title("URL")
window.geometry("1100x300")

label = Label(
    window,
    text=url,
    font=("Comic Sans MS", 65),
    fg="red"
)
label.pack()
window.mainloop()