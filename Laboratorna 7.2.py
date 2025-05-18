from tkinter import *
from math import *

def main(event):
    # Отримання значень з полів введення
    getm = value.get()
    getn = value1.get()
    
    # Перевірка, чи обидва значення введені
    if getm and getn:
        try:
            m = float(getm)
            n = float(getn)
            algo(m, n)
        except ValueError:
            l_answer["text"] = "Помилка: введіть коректні числові значення"

def algo(m, n):
    # Розрахунок
    try:
        a = (sqrt(m + 3 * n)) / 9.3
        y = m * n - 8
        z = (n - 3 * m) / 2
        # Виведення результату
        l_answer["text"] = f"Відповідь:\na = {a:.2f}\ny = {y:.2f}\nz = {z:.2f}" 
    except:
        l_answer["text"] = f"M або N < 0"

# Створення головного вікна
root = Tk()
root.title("Laboratora 6")
root.geometry("400x350")
w = 400
h = 450
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(width = False, height= False)

# Змінні
value = StringVar()
value1 = StringVar()
value2 = StringVar()

# Перший комплект
frame1 = Frame(root)
frame1.pack(fill=X)

l1 = Label(frame1, text='Введіть значення M =')
l1.pack(side=LEFT, padx=5, pady=5)

e1 = Entry(frame1, textvariable=value)
e1.pack(side=LEFT, padx=5, pady=5)
e1.insert(0, "0")
# Другий комплект
frame2 = Frame(root)
frame2.pack(fill=X)

l2 = Label(frame2, text='Введіть значення N =')
l2.pack(side=LEFT, padx=5, pady=5)

e2 = Entry(frame2, textvariable=value1)
e2.pack(side=LEFT, padx=5, pady=5)
e2.insert (0, "0")

# Кнопка розрахунків
b1 = Button(frame2, text="Обчислити")
b1.pack(side=LEFT, padx=5, pady=5)
b1.bind('<Button-1>', main)

# Умова
l_default = Label(root, text='Умови рівнянь \n  √(m + 3n)\n x = --------------\n    9,3\n\n y = mn - 8 \n\n   n - 3m\n z = --------\n      2')
l_default.pack(side=TOP, padx = 5, pady=5)

#Відповідь

l_answer = Label(root, text = "")
l_answer.pack (side=TOP, padx=5, pady=5)
# Запуск головного циклу
root.mainloop()
