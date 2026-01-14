from tkinter import *
window = Tk()
window.title("Text Generator Simple")
window.geometry("1100x300")

label = Label(
    window,
    text="Text Generator Simple",
    font=("Impact", 75),
    fg="red"
)
label.pack()
window.mainloop()
bimbows = Tk()
bimbows.title("Text Generator Simple")
bimbows.geometry("1920x1200")
text = input("Text: ")
babel = Label(
    bimbows,
    text=text,
    font=("Impact", 75),
    fg="red"
)
babel.pack()
babel = Label(
    bimbows,
    text="Text Generator Simple",
    font=("Impact", 20),
    fg="red"
)
babel.pack()
bimbows.mainloop()
exit()