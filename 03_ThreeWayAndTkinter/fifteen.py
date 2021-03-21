import tkinter as tk
from tkinter import messagebox as mbox
from itertools import product
from random import shuffle


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('Feefteen')
        self.rows=4
        self.cols=4
        self.buttons=self.rows*self.cols-1
        self.create_widgets()
        self.grid_reconfigure()
        self.new_game()

    def create_widgets(self):
        self.new = tk.Button(self, text='New', command=self.new_game)
        self.new.grid(row=0, column=0, columnspan=2)
        self.exit = tk.Button(self, text='Exit', command=self.quit)
        self.exit.grid(row=0, column=2, columnspan=2)
        self.button = [tk.Button(self, text=str(i+1)) for i in range(self.buttons)]
        for b in self.button:
            b.configure(command=self.move(b))

    def grid_reconfigure(self):
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky="NSEW")

        for i in range(self.rows):
            self.rowconfigure(i+1, weight=1)
        for i in range(self.cols):
            self.columnconfigure(i, weight=1)

    def new_game(self):
        pos = list(product(range(1, self.rows+1), range(self.cols)))
        shuffle(pos)
        for b, (r, c) in zip(self.button, pos):
            b.grid(row=r, column=c, sticky="NSEW")
        self.empty_pos = pos[-1]

    def move(self, button):
        def f():
            re, ce = self.empty_pos
            rb, cb = button.grid_info()['row'], button.grid_info()['column']
            if rb == re and (cb == ce+1 or cb == ce-1) or cb == ce and (rb == re+1 or rb == re-1):
                button.grid(row=re, column=ce)
                self.empty_pos = rb, cb
                if self.win():
                    self.victory()
        return f

    def win(self):
        for b in self.button:
            # number on button
            lbl = int(b['text']) - 1
            # number of button position
            pos = self.cols * (b.grid_info()['row'] - 1) + b.grid_info()['column']
            if lbl != pos:
                return False
        return True

    def victory(self):
        mbox.showinfo("Victory", "You win!")
        self.new_game()

if (__name__ == "__main__"):
    app = Application()
    app.mainloop()
