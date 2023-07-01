import tkinter as tk
from button import Button

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.display = tk.Entry(self.window, width=20)
        self.display.grid(row=0, column=0, columnspan=4)
        self.buttons = self.create_buttons()

    def create_buttons(self):
        buttons = []
        colors = ['red', 'green', 'blue', 'yellow']
        for i in range(1, 10):
            button = Button(self.window, text=str(i), bg=colors[i%4], command=lambda i=i: self.update_display(i))
            buttons.append(button)
        return buttons

    def update_display(self, value):
        self.display.insert(tk.END, str(value))

    def run(self):
        self.window.mainloop()
