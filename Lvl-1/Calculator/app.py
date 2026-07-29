import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")
root.resizable(False, False)


BG_DARK = "#1e1e1e"
DISPLAY_BG = "#2b2b2b"
BTN_NUM = "#333333"
BTN_NUM_ACTIVE = "#4a4a4a"
BTN_OP = "#ff9500"
BTN_OP_ACTIVE = "#ffb143"
BTN_FUNC = "#a5a5a5"
BTN_FUNC_ACTIVE = "#c7c7c7"
FG_WHITE = "white"
FG_BLACK = "#1e1e1e"

style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background=BG_DARK)

style.configure(
    "Display.TLabel",
    background=DISPLAY_BG,
    foreground="white",
    font=("Arial", 40),
    anchor="e",
    padding=(15, 20),
)


style.configure(
    "Num.TButton",
    background=BTN_NUM,
    foreground=FG_WHITE,
    font=("Arial", 20),
    borderwidth=0,
    focusthickness=0,
    padding=15,
)
style.map("Num.TButton", background=[("active", BTN_NUM_ACTIVE)])


style.configure(
    "Op.TButton",
    background=BTN_OP,
    foreground=FG_WHITE,
    font=("Arial", 22, "bold"),
    borderwidth=0,
    focusthickness=0,
    padding=15,
)
style.map("Op.TButton", background=[("active", BTN_OP_ACTIVE)])


style.configure(
    "Func.TButton",
    background=BTN_FUNC,
    foreground=FG_BLACK,
    font=("Arial", 18, "bold"),
    borderwidth=0,
    focusthickness=0,
    padding=15,
)
style.map("Func.TButton", background=[("active", BTN_FUNC_ACTIVE)])

root.configure(background=BG_DARK)


expression = ""
just_evaluated = False

OP_SYMBOLS = {"+": "+", "-": "−", "*": "×", "/": "÷"}


def format_display(expr: str) -> str:
    """برای نمایش زیباتر عملگرها در صفحه نمایش"""
    disp = expr
    for real, pretty in OP_SYMBOLS.items():
        disp = disp.replace(real, f" {pretty} ")
    return disp if disp else "0"


def update_display():
    display.config(text=format_display(expression))


def press_number(num):
    global expression, just_evaluated
    if just_evaluated:
        expression = ""
        just_evaluated = False
    expression += str(num)
    update_display()


def press_dot():
    global expression, just_evaluated
    if just_evaluated:
        expression = ""
        just_evaluated = False

    last_part = expression.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]
    if "." not in last_part:
        expression += "0." if expression == "" or expression[-1] in "+-*/" else "."
        update_display()


def clear():
    global expression, just_evaluated
    expression = ""
    just_evaluated = False
    display.config(text="0")


def backspace():
    global expression, just_evaluated
    if just_evaluated:
        clear()
        return
    expression = expression[:-1]
    update_display()


def toggle_sign():
    global expression
    if not expression:
        return
    if expression.startswith("-"):
        expression = expression[1:]
    else:
        expression = "-" + expression
    update_display()


def percent():
    global expression
    try:
        result = eval(expression) / 100
        expression = format_number(result)
        update_display()
    except Exception:
        clear()
        display.config(text="خطا")


def operation(op):
    global expression, just_evaluated
    if not expression:
        return
    just_evaluated = False
    if expression[-1] in "+-*/":
        expression = expression[:-1] + op
    else:
        expression += op
    update_display()


def format_number(num):
    if isinstance(num, float) and num.is_integer():
        return str(int(num))
    return str(round(num, 10))


def calculate():
    global expression, just_evaluated
    try:
        if not expression or expression[-1] in "+-*/":
            return
        result = eval(expression)
        expression = format_number(result)
        update_display()
        just_evaluated = True
    except ZeroDivisionError:
        display.config(text="تقسیم بر صفر!")
        expression = ""
        just_evaluated = True
    except Exception:
        display.config(text="خطا")
        expression = ""
        just_evaluated = True



show = ttk.Frame(root, padding=(15, 20, 15, 10))
show.grid(row=0, column=0, sticky="nsew")
show.grid_columnconfigure(0, weight=1)

display = ttk.Label(show, text="0", style="Display.TLabel")
display.grid(row=0, column=0, sticky="ew")


func_frame = ttk.Frame(root, padding=(10, 0, 10, 5))
func_frame.grid(row=1, column=0, sticky="nsew")

func_buttons = [
    ("C", clear),
    ("+/-", toggle_sign),
    ("%", percent),
    ("⌫", backspace),
]

for col, (text, cmd) in enumerate(func_buttons):
    ttk.Button(func_frame, text=text, style="Func.TButton", command=cmd).grid(
        row=0, column=col, padx=5, pady=5, sticky="nsew"
    )
    func_frame.grid_columnconfigure(col, weight=1)


main_frame = ttk.Frame(root, padding=(10, 0, 10, 15))
main_frame.grid(row=2, column=0, sticky="nsew")

layout = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    [".", "0", "=", "+"],
]

for r, row_items in enumerate(layout):
    for c, item in enumerate(row_items):
        if item.isdigit():
            btn = ttk.Button(
                main_frame, text=item, style="Num.TButton",
                command=lambda x=item: press_number(x)
            )
        elif item == ".":
            btn = ttk.Button(
                main_frame, text=".", style="Num.TButton", command=press_dot
            )
        elif item == "=":
            btn = ttk.Button(
                main_frame, text="=", style="Op.TButton", command=calculate
            )
        else:
            btn = ttk.Button(
                main_frame, text=OP_SYMBOLS[item], style="Op.TButton",
                command=lambda x=item: operation(x)
            )
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

for i in range(4):
    main_frame.grid_columnconfigure(i, weight=1)
for i in range(4):
    main_frame.grid_rowconfigure(i, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)


def on_key(event):
    ch = event.char
    if ch.isdigit():
        press_number(ch)
    elif ch in "+-*/":
        operation(ch)
    elif ch == ".":
        press_dot()
    elif ch in ("\r", "="):
        calculate()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym.lower() == "escape" or ch.lower() == "c":
        clear()


root.bind("<Key>", on_key)

root.mainloop()