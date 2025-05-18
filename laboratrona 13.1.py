import random
from tkinter import *

def new_RandomNumbers():
    new_randomNumbers = []
    for i in range(4):
        new_randomNumbers.append(random.randint(10, 40))
        randomNumbers.append(new_randomNumbers[i])
    show_new_window(randomNumbers, new_randomNumbers)

def RandomNumbers():
    global randomNumbers
    randomNumbers = []
    for i in range(10):
        randomNumbers.append(random.randint(10, 40))
    sumOfNumbers(randomNumbers)

def sumOfNumbers(randomNumbers):
    total_sum = sum(randomNumbers)
    main(randomNumbers, total_sum)

def show_new_window(randomNumbers, new_randomNumbers):
    new_window = Toplevel()
    new_window.title("Додані значення")
    new_window.geometry("350x350")
    
    label_original = Label(new_window, text="Основні 10 значень масиву:")
    label_original.pack(side=TOP, padx=5, pady=5)
    
    for i in range(10):
        label_numbers = Label(new_window, text=f"Index: {i}, Number: {randomNumbers[i]}")
        label_numbers.pack(side=TOP, padx=5, pady=0)
    
    label_added = Label(new_window, text="\nДодані 4 значення:")
    label_added.pack(side=TOP, padx=5, pady=5)
    
    for i in range(4):
        label_new_numbers = Label(new_window, text=f"Index: {i + 10}, Number: {new_randomNumbers[i]}")
        label_new_numbers.pack(side=TOP, padx=5, pady=0)

def main(randomNumbers, total_sum):
    root = Tk()
    root.title("Main")
    root.geometry("350x350")
    w = 350
    h = 350
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)
    frame_top = Frame(root)
    frame_top.pack(fill=X)

    

    label_top = Label(frame_top, text="Початкові данні: ")
    label_top.pack(side=TOP, padx=5, pady=5)

    label_default = Label(text=f"a = 10, b = 40 ")
    label_default.pack(side=TOP, padx=5, pady=0)

    frame_head = Frame(root)
    frame_head.pack(fill=X)

    label_head = Label(frame_head, text="Вивід результату")
    label_head.pack(side=TOP, padx=5, pady=5)

    for i in range(10):
        label_numbers = Label(text=f"Index of number: {i}, number is: {randomNumbers[i]}")
        label_numbers.pack(side=TOP, padx=5, pady=0)
    label_sum = Label(text=f"Sum of numbers: {total_sum}")
    label_sum.pack(side=TOP, padx=5, pady=0)

    update_buttom = Button(root, text="Update", command=new_RandomNumbers)  # Передаємо посилання на функцію
    update_buttom.pack(side=TOP, padx=5, pady=5)
    exit_buttom = Button(root, text="Exit", command=root.quit)
    exit_buttom.pack(side=TOP, padx=5, pady=5)
    root.mainloop()

RandomNumbers()