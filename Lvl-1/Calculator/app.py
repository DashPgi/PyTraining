import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x550")
root.title("Calculator")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TFrame",
    background="#1e1e1e"
)

style.configure(
    "TLabel",
    background="#1e1e1e",
    foreground="white",
    font=("Arial", 25)
)

style.configure(
    "TButton",
    background="#333333",
    foreground="white",
    font=("Arial", 16),
    padding=10
)

style.map(
    "TButton",
    background=[("active", "#555555")]
)

root.configure(background="#1e1e1e")


value = ""


def press(num):
    global value
    value += str(num)
    display.config(text=value)


def clear():
    global value
    value = ""
    display.config(text="")


def operation(op):
    global value
    value += op
    display.config(text=value)


show = ttk.Frame(root, padding=20)
show.grid(row=0, column=0)

display = ttk.Label(
    show,
    text="",
    width=15,
    anchor="e"
)

display.grid()


cp = ttk.Frame(root, padding=10)
cp.grid(row=1, column=0)

operations = [
    ("+", "+"),
    ("-", "-"),
    ("*", "*"),
    ("/", "/")
]

for col, (text, value_op) in enumerate(operations):
    ttk.Button(
        cp,
        text=text,
        command=lambda x=value_op: operation(x)
    ).grid(
        row=0,
        column=col,
        padx=5,
        pady=5
    )


frame = ttk.Frame(root, padding=10)
frame.grid(row=2, column=0)


for i in range(1, 10):
    ttk.Button(
        frame,
        text=str(i),
        command=lambda x=i: press(x)
    ).grid(
        row=(i-1)//3,
        column=(i-1)%3,
        padx=5,
        pady=5,
        sticky="nsew"
    )


ttk.Button(
    frame,
    text="0",
    command=lambda: press(0)
).grid(
    row=3,
    column=1,
    padx=5,
    pady=5,
    sticky="nsew"
)


ttk.Button(
    frame,
    text="C",
    command=clear
).grid(
    row=3,
    column=0,
    padx=5,
    pady=5,
    sticky="nsew"
)


for i in range(3):
    frame.grid_columnconfigure(i, weight=1)

for i in range(4):
    frame.grid_rowconfigure(i, weight=1)


root.grid_columnconfigure(0, weight=1)


root.mainloop()