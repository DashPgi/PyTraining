import tkinter as tk
from tkinter import ttk

root = tk.Tk()
show = ttk.Frame(root,padding=60)
style = ttk.Style()
frame = ttk.Frame(root,padding=50)

root.geometry("500x600")
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

show.grid(row=0, column=0, pady=20)

frame.grid(row=1, column=0)

label = ttk.Label(show, text="")
label.grid()

for i in range(1, 10):
    ttk.Button(
        frame,
        text=str(i),
        command=lambda x=i: label.config(text=x)
    ).grid(
        row=(i - 1) // 3,
        column=(i - 1) % 3,
        padx=5,
        pady=5,
        sticky="nsew"
    )

ttk.Button(
    frame,
    text="0",
    command=lambda x=0: label.config(text=x)
).grid(
    row=3,
    column=1,
    padx=5,
    pady=5,
    sticky="nsew"
)
for i in range(3):
    frame.grid_columnconfigure(i, weight=1)
for i in range(4):
    frame.grid_rowconfigure(i, weight=1)

style = ttk.Style()

style.theme_use("clam")

style.configure(
    ".",
    background="#1e1e1e",
    foreground="white",
    fieldbackground="#1e1e1e"
)

style.configure(
    "TFrame",
    background="#1e1e1e",
    padding="10"
)

style.configure(
    "TLabel",
    background="#1e1e1e",
    foreground="white",
    font=("Arial", 18)
)

style.configure(
    "TButton",
    background="#333333",
    foreground="white",
    font=("Arial", 16),
    padding=10,
    borderradius=100
)

style.map(
    "TButton",
    background=[
        ("active", "#555555")
    ]
)

root.configure(background="#1e1e1e")

root.mainloop()
