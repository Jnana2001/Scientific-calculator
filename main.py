import tkinter as tk
import math


class Calculator:
    def __init__(self, calculate):
        self.calculate = calculate
        calculate.title("Scientific Calculator")
        calculate.geometry("400x500")

        self.total = tk.StringVar()

        self.entry = tk.Entry(calculate, textvariable=self.total, font=("bold", 20))
        self.entry.grid(row=0, column=0, columnspan=5, pady=5)

        self.create_buttons()

    def create_buttons(self):
        button_list = [
            ['sin', 'cos', 'tan', '^2', '10^x'],
            ['7', '8', '9', '/', 'log(x)'],
            ['4', '5', '6', '*', '1/x'],
            ['1', '2', '3', '-', 'x!'],
            ['0', 'C', '=', '+', 'sqrt']
        ]

        for i, row in enumerate(button_list):
            for j, button_text in enumerate(row):
                button = tk.Button(
                    self.calculate, text=button_text, width=5, height=3, font=("Helvetica", 20),
                    command=lambda text=button_text: self.click(text)
                )
                button.grid(row=i + 1, column=j, sticky="nsew")
            self.calculate.rowconfigure(i + 1, weight=1)
        self.calculate.columnconfigure(0, weight=1)
        self.calculate.columnconfigure(1, weight=1)
        self.calculate.columnconfigure(2, weight=1)
        self.calculate.columnconfigure(3, weight=1)
        self.calculate.columnconfigure(4, weight=1)

    def click(self, button_text):
        if button_text == '=':
            try:
                result = eval(self.entry.get())
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'C':
            self.total.set("")
        elif button_text == 'sin':
            try:
                result = math.sin(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'cos':
            try:
                result = math.cos(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'tan':
            try:
                result = math.tan(math.radians(float(self.entry.get())))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == '^2':
            try:

                result = float(self.entry.get()) ** 2
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'log(x)':
            try:
                result = math.log(float(self.entry.get()))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == '1/x':
            try:
                result = 1 / float(self.entry.get())
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'x!':
            try:
                result = math.factorial(int(self.entry.get()))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == '10^x':
            try:
                result = 10 ** float(self.entry.get())
                self.total.set(result)
            except:
                self.total.set("Error")
        elif button_text == 'sqrt':
            try:
                result = math.sqrt(float(self.entry.get()))
                self.total.set(result)
            except:
                self.total.set("Error")
        else:
            self.total.set(self.entry.get() + button_text)


if __name__ == '__main__':
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()
