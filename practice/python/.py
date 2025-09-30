

# --- Command Line Calculator ---
def cli_calculator():
    while True:
        opperation = input("Enter an operation (+, -, *, /) or 'q' to quit: ")
        if opperation == "q":
            print("Thank you for using the calculator!")
            break
        if opperation not in ("+", "-", "*", "/"):
            print("Invalid operation. Please enter one of (+, -, *, /) or 'q' to quit.")
            continue
        try:
            x = float(input("Enter a number: "))
            y = float(input("Enter another number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue
        if opperation == "+":
            print(f"{x} + {y} = {x + y}")
        elif opperation == "-":
            print(f"{x} - {y} = {x - y}")
        elif opperation == "*":
            print(f"{x} * {y} = {x * y}")
        elif opperation == "/":
            if y != 0:
                print(f"{x} / {y} = {x / y}")
            else:
                print("Error: Division by zero is not allowed.")

# --- Tkinter GUI Calculator ---
import tkinter as tk
from tkinter import messagebox

def evaluate(expr):
    try:
        # Only allow safe characters
        allowed = set("0123456789+-*/.() ")
        if not set(expr) <= allowed:
            return "Err"
        result = eval(expr)
        return str(result)
    except ZeroDivisionError:
        return "Err: Div0"
    except Exception:
        return "Err"

def run_gui():
    root = tk.Tk()
    root.title("Simple Calculator")
    root.geometry("300x400")

    expr = tk.StringVar()

    entry = tk.Entry(root, textvariable=expr, font=("Arial", 20), bd=8, relief=tk.RIDGE, justify='right')
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    def on_click(val):
        if val == 'C':
            expr.set("")
        elif val == '=':
            res = evaluate(expr.get())
            expr.set(res)
        else:
            expr.set(expr.get() + val)

    buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', '.', 'C', '+'],
        ['=']
    ]

    for r, row in enumerate(buttons, 1):
        for c, char in enumerate(row):
            tk.Button(root, text=char, width=5, height=2, font=("Arial", 18),
                      command=lambda v=char: on_click(v)).grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

    # Make the grid expand
    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    mode = input("Type 'gui' for graphical calculator, or anything else for command line: ").strip().lower()
    if mode == 'gui':
        run_gui()
    else:
        cli_calculator()