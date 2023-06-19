import tkinter as tk
import math
#tkinter is a GUI toolkit for python that provides necessary libraries and tools for creating GUI based application.
#tkinter has a user interface buttons for different mathematical operators like add,sub,multiply,div,log,factorials and trignometric functions.
class Calculator:
    def __init__(self, calculate):
        #defining a class calculator 
        self.calculate = calculate
        calculate.title("Scientific Calculator")
        calculate.geometry("400x500")
        #Setting a title and geometry(height and width) of a calculator
        self.total = tk.StringVar()

        self.entry = tk.Entry(calculate, textvariable=self.total, font=("bold", 20))
        self.entry.grid(row=0, column=0, columnspan=5, pady=5)
        #Entry filed is implemted using tk.Entry
        self.create_buttons()
        
    def create_buttons(self):
        #creating a list of buttons
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
                #widget and buttons are implemented as tk.button widgets 
                button.grid(row=i + 1, column=j, sticky="nsew")
            self.calculate.rowconfigure(i + 1, weight=1)
        self.calculate.columnconfigure(0, weight=1)
        self.calculate.columnconfigure(1, weight=1)
        self.calculate.columnconfigure(2, weight=1)
        self.calculate.columnconfigure(3, weight=1)
        self.calculate.columnconfigure(4, weight=1)
        #The layout and appearance of the calculator are managed by the grid,rowconfigure and columnconfigure methods
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
         # using elif different oprrations for the buttons are created

if __name__ == '__main__':
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()
#The calculator GUI is created and runs in a loop until the user closes the window
