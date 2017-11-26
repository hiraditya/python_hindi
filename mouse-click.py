# How to add mouse events
import tkinter as tk


def left_click(event):
    print("leftClick")


def right_click(event):
    print("rightClick")


w = tk.Tk()
f = tk.Frame(w, width=300, height=300)
l = tk.Label(w, text="Hello world")

f.bind("<Button-1>", left_click)
f.bind("<Button-3>", right_click)

f.pack()
l.pack()
# event loop
w.mainloop()
