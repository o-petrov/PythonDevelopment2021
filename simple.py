import time
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.mode, self.other_mode = "%c", "%Y%m%d(%w)%H%M%S"
        self.grid()
        self.createWidgets()
        self.showtime()

    def showtime(self):
        self.time.set(time.strftime(self.mode))

    def swap(self):
        self.mode, self.other_mode = self.other_mode, self.mode
        self.showtime();

    def createWidgets(self):
        self.time = tk.StringVar()

        self.timeButton = tk.Button(self, text='Time', command=self.showtime)
        self.modeButton = tk.Button(self, text='Mode', command=self.swap)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)

        self.timeLabel = tk.Label(self, textvariable=self.time)

        self.timeButton.grid()
        self.modeButton.grid(row=0, column=1)
        self.quitButton.grid(row=0, column=2)
        self.timeLabel.grid(columnspan=3)


if (__name__ == "__main__"):
    app = Application()
    app.master.title('Sample application')
    app.mainloop()
