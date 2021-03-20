import time
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.rows=4
        self.cols=4
        self.buttons=self.rows*self.cols-1
        self.create_widgets()

    def create_widgets(self):
        self.new = tk.Button(self, text='New')
        self.new.grid(row=0, column=0, columnspan=2)
        self.exit = tk.Button(self, text='Exit')
        self.exit.grid(row=0, column=2, columnspan=2)

        self.button = [tk.Button(self, text=str(i+1)) for i in range(self.buttons)]
        for i in range(self.buttons):
            self.button[i].grid(row=1+i//self.rows, column=i%self.rows, sticky="NSEW")

        self.grid_reconfigure()

    def grid_reconfigure(self):
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky="NSEW")

        for i in range(self.rows):
            self.rowconfigure(i+1, weight=1)
        for i in range(self.cols):
            self.columnconfigure(i, weight=1)


if (__name__ == "__main__"):
    app = Application()
    app.master.title('Пятнашки')
    app.mainloop()
