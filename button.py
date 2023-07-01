import tkinter as tk

class Button(tk.Button):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.grid()
