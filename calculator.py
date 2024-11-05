import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.configure(bg='#1a472a')
        
        # Entry field
        self.display = tk.Entry(root, width=30, font=('Arial', 20), 
                              bg='#d5f4e6', fg='#0a2f1f', 
                              justify='right', bd=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Button style
        style = ttk.Style()
        style.configure('Calc.TButton',
                       padding=10,
                       font=('Arial', 12),
                       background='#2d8659',
                       foreground='#ffffff')
        
        # Buttons layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('^', 5, 3),
            ('√', 6, 0), ('(', 6, 1), (')', 6, 2), ('C', 6, 3)
        ]
        
        for (text, row, col) in buttons:
            button = ttk.Button(root, text=text, style='Calc.TButton',
                              command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
        
        # Configure grid weights
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        current = self.display.get()
        
        if value == 'C':
            self.display.delete(0, tk.END)
        elif value == '=':
            try:
                # Replace scientific functions with math module calls
                expr = current.replace('sin', 'math.sin')
                expr = expr.replace('cos', 'math.cos')
                expr = expr.replace('tan', 'math.tan')
                expr = expr.replace('^', '**')
                expr = expr.replace('√', 'math.sqrt')
                
                result = eval(expr)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, value)

def main():
    root = tk.Tk()
    root.geometry("400x600")
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()