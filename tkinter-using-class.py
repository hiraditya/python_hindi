# Using class create GUI applications

from tkinter import *

# Object oriented programming
#   Data abstraction and encapsulation
class CreateButtons:
    def __init__(self, parent):
        f = Frame(parent)
        f.pack()
        self.print_button = Button(f, text="Print", command=self.print_list)
        self.print_button.pack(side=LEFT)
        self.quit_button = Button(f, text="Quit", command=f.quit)
        self.quit_button.pack(side=LEFT)

    def print_list(self):
        print("Print button was clicked")


root = Tk()
root.geometry("500x300")
c = CreateButtons(root) # External user of CreateButton
root.mainloop()

# Create a question and multiple choice options of which one is correct
# When correct option is clicked a message displays that option is correct!