import tkinter as tk
import sqlite3

con = sqlite3.connect("example.db")
cur = con.cursor()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                command=self.master.destroy)
        self.quit.pack(side="bottom")

        for i in range(5):
            for j in range(5):
                b = tk.Entry(root, text="")
                b.grid(row=i, column=j)

    def say_hi(self):
        for row in cur.execute("SELECT * FROM Customer"):
            print(row)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
