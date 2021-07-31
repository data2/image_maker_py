from tkinter import *

window = Tk()
window.title("First Window")
window.geometry("520x320")
txt = Entry(window, width=30)
txt.grid(column=30, row=30)
def clicked():
    res = "Welcome to " + txt.get()

btn = Button(window, text="生成", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()