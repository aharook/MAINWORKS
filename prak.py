from tkinter import *

def safe_op(operation):
    try:
        a_val = float(value1.get())
        b_val = float(value2.get())
        operation(a_val, b_val)
    except ValueError:
        lbl3["text"] = "❌ Помилка: введіть коректні числові значення"

def show_result(a, b, result, op_name):
    lbl3["text"] = f"✅ {op_name}:\na = {a:.2f}\nb = {b:.2f}\nРезультат: {result:.2f}"

def sum(a, b):
    show_result(a, b, a + b, "Сума")

def min(a, b):
    show_result(a, b, a - b, "Різниця")

def mult(a, b):
    show_result(a, b, a * b, "Добуток")

def div(a, b):
    if b != 0:
        show_result(a, b, a / b, "Частка")
    else:
        lbl3["text"] = "❌ Помилка: ділення на нуль"

# --- Кольори ---
BG_COLOR = "#2c3e50"
TEXT_COLOR = "#ecf0f1"
BTN_COLOR = "#3498db"
ENTRY_BG = "#ecf0f1"
ENTRY_FG = "#2c3e50"

# --- GUI ---
root = Tk()
root.title(" AHAROOK`S CALCULATOR ")
root.geometry("450x450")
w = 450
h = 450
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(width=False, height=False)
root.configure(bg=BG_COLOR)

frame_top = Frame(root, bg=BG_COLOR)
frame_top.pack(fill=X)

frame2 = Frame(root, bg=BG_COLOR)
frame2.pack(fill=X)

frame3 = Frame(root, bg=BG_COLOR)
frame3.pack(fill=X)

value1 = StringVar()
value2 = StringVar()

lbl1 = Label(frame_top, text="введіть значення a =", fg=TEXT_COLOR, bg=BG_COLOR)
lbl1.pack(side=LEFT, padx=5, pady=5)
e1 = Entry(frame_top, textvariable=value1, bg=ENTRY_BG, fg=ENTRY_FG)
e1.pack(side=LEFT, padx=5, pady=5)
e1.insert(0, "0")

lbl2 = Label(frame2, text="введіть значення b =", fg=TEXT_COLOR, bg=BG_COLOR)
lbl2.pack(side=LEFT, padx=5, pady=5)
e2 = Entry(frame2, textvariable=value2, bg=ENTRY_BG, fg=ENTRY_FG)
e2.pack(side=LEFT, padx=5, pady=5)
e2.insert(0, "0")

lbl_text = Label(frame3, text="Оберіть операцію:", fg=TEXT_COLOR, bg=BG_COLOR)
lbl_text.pack(side=TOP, padx=5, pady=5)

btn_sum = Button(frame3, text="Сума", command=lambda: safe_op(sum), bg=BTN_COLOR, fg="white")
btn_sum.pack(side=LEFT, padx=5, pady=5)

btn_min = Button(frame3, text="Різниця", command=lambda: safe_op(min), bg=BTN_COLOR, fg="white")
btn_min.pack(side=LEFT, padx=5, pady=5)

btn_mult = Button(frame3, text="Добуток", command=lambda: safe_op(mult), bg=BTN_COLOR, fg="white")
btn_mult.pack(side=LEFT, padx=5, pady=5)

btn_div = Button(frame3, text="Частка", command=lambda: safe_op(div), bg=BTN_COLOR, fg="white")
btn_div.pack(side=LEFT, padx=5, pady=5)

lbl3 = Label(root, text="Відповідь:", fg=TEXT_COLOR, bg=BG_COLOR)
lbl3.pack(side=TOP, padx=5, pady=15)

root.mainloop()
