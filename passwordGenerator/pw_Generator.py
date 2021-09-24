import random
from tkinter import *


class passwordGen:

    def __init__(self, master):
        frame = Frame(master)  # add parent for Frame
        frame.pack()

        self.printButton = Button(frame, text="Generate Password", padx=4, pady=4, command=self.pw_gen)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Close", padx=4, pady=4, command=master.destroy)
        self.quitButton.pack(side=LEFT)

        self.output = Label(master, fg="Green")
        self.output.pack()

        self.pw_gen()

    def pw_gen(self):
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "[]{}()*;/,_-."

        all = lower + upper + numbers + symbols

        length = 16

        password = "".join(random.sample(all,length))
        self.output.config(text=password)

root = Tk()
passwordGen(root)
root.mainloop()