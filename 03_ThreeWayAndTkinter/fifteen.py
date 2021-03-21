import tkinter as tk
from itertools import product
from random import shuffle


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.rows=4
        self.cols=4
        self.buttons=self.rows*self.cols-1
        self.pos = list(product(range(1, self.rows+1), range(self.cols)))
        self.create_widgets()
        self.grid_reconfigure()
        self.new_game()

    def create_widgets(self):
        self.new = tk.Button(self, text='New', command=self.new_game)
        self.new.grid(row=0, column=0, columnspan=2)
        self.exit = tk.Button(self, text='Exit', command=self.quit)
        self.exit.grid(row=0, column=2, columnspan=2)
        self.button = [tk.Button(self, text=str(i+1)) for i in range(self.buttons)]

    def grid_reconfigure(self):
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky="NSEW")

        for i in range(self.rows):
            self.rowconfigure(i+1, weight=1)
        for i in range(self.cols):
            self.columnconfigure(i, weight=1)

    def new_game(self):
        shuffle(self.pos)
        for b, (r, c) in zip(self.button, self.pos):
            b.grid(row=r, column=c, sticky="NSEW")


if (__name__ == "__main__"):
    app = Application()
    app.master.title('Пятнашки')
    app.mainloop()
