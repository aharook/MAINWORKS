from tkinter import *
from math import *


# Налаштування вікна
root = Tk()
root.title("Main")
root.geometry("350x350")
w = 350
h = 350
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(width = False, height= False)

used_test1 = False
used_test2 = False
used_test3 = False
used_test4 = False
used_test5 = False

result = 0  # Кількість вірних відповідей
tests_passed = 0  # Кількість пройдених тестів

# Функція для оновлення лейблів
def update_labels():
    label_final["text"] = f"Пройдено тестів {tests_passed}/5"
    label_score["text"] = f"Балів - {result * 2}/10"  # Бали подвоюються

def test1():
    global used_test1
    sub1 = Tk()
    sub1.title("Test1")
    sub1.geometry("340x200")
    sub1.resizable(width=False, height=False)

    frame_subtest1 = Frame(sub1)
    frame_subtest1.pack(fill=X)

    label_subtest1 = Label(frame_subtest1, text="Чи точно викладач Шпортько О.В. найкращий викладач?")
    label_subtest1.pack(side=TOP, padx=5, pady=5)

    label_showtest1 = Label(sub1, text="")
    label_showtest1.pack(side=BOTTOM, padx=5, pady=5)

    select_test1 = StringVar(value="")
    options = ["Самособою", "Так, точно", "НЕПЕРЕВЕРШЕНИЙ!!!"]

    for option in options:
        radio_button_test1 = Radiobutton(sub1, text=option, variable=select_test1, value=option)
        radio_button_test1.pack(anchor="w", side=TOP)

    if not used_test1:
        button_answertest1 = Button(sub1, text="Відповісти", command=lambda: answer_test1(select_test1.get(), label_showtest1, sub1))
        button_answertest1.pack(side=TOP, padx=5, pady=5)

def answer_test1(selection, label, window):
    global used_test1, result, tests_passed
    used_test1 = True
    tests_passed += 1
    result += 1  # Додаємо бал незалежно від відповіді
    label["text"] = "Відповідь вірна"  # Завжди виводимо, що відповідь вірна
    update_labels()  # Оновлюємо лейбли
    window.after(2000, window.destroy)  # Закриття вікна через 2 секунди

def test2():
    global used_test2
    sub2 = Tk()
    sub2.title("Test2")
    sub2.geometry("300x200")
    sub2.resizable(width=False, height=False)

    frame_subtest2 = Frame(sub2)
    frame_subtest2.pack(fill=X)

    label_subtest2 = Label(frame_subtest2, text="2+2=?")
    label_subtest2.pack(side=TOP, padx=5, pady=5)

    label_showtest2 = Label(sub2, text="")
    label_showtest2.pack(side=BOTTOM, padx=5, pady=5)

    if not used_test2:
        entry_answertest2 = Entry(sub2)
        entry_answertest2.pack(side=TOP, padx=5, pady=5)

        button_answertest2 = Button(sub2, text="Ввести", command=lambda: answer_test2(entry_answertest2.get(), label_showtest2, sub2))
        button_answertest2.pack(side=TOP, padx=5, pady=5)

def answer_test2(value, label, window):
    global used_test2, result, tests_passed
    if value:
        used_test2 = True
        tests_passed += 1
        subanswer_test2(value, label, window, result)
    else : 
        label["text"] = "Введіть дійсне число"
def subanswer_test2(value, label, window, result) :
    try:
        if int(value) == 4:
            result += 1
            label["text"] = "Відповідь вірна"
        else:
            label["text"] = "Відповідь не вірна"
    except ValueError:
        label["text"] = "Введіть числове значення"
    update_labels()  # Оновлюємо лейбли
    window.after(2000, window.destroy)  # Закриття вікна через 2 секунди

def test3():
    global used_test3
    sub3 = Tk()
    sub3.title("Test3")
    sub3.geometry("300x200")
    sub3.resizable(width=False, height=False)

    frame_subtest3 = Frame(sub3)
    frame_subtest3.pack(fill=X)

    label_subtest3 = Label(frame_subtest3, text="Чи вмієте ви читати?")
    label_subtest3.pack(side=TOP, padx=5, pady=5)

    label_showtest3 = Label(sub3, text="")
    label_showtest3.pack(side=BOTTOM, padx=5, pady=5)

    frame_answertest3 = Frame(sub3)
    frame_answertest3.pack(fill=X)

    if not used_test3:
        button_answertest3_yes = Button(frame_answertest3, text="Так", command=lambda: answer_test3(True, label_showtest3, sub3))
        button_answertest3_yes.pack(side=LEFT, padx=5, pady=5)

        button_answertest3_no = Button(frame_answertest3, text="!@#$%", command=lambda: answer_test3(False, label_showtest3, sub3))
        button_answertest3_no.pack(side=RIGHT, padx=5, pady=5)

def answer_test3(correct, label, window):
    global used_test3, result, tests_passed
    used_test3 = True
    tests_passed += 1
    if correct:
        result += 1
        label["text"] = "Відповідь вірна"
    else:
        label["text"] = "Відповідь не вірна"
    update_labels()  # Оновлюємо лейбли
    window.after(2000, window.destroy)  # Закриття вікна через 2 секунди

def test4():
    global used_test4
    sub4 = Tk()
    sub4.title("Test4")
    sub4.geometry("300x200")
    sub4.resizable(width=False, height=False)

    frame_subtest4 = Frame(sub4)
    frame_subtest4.pack(fill=X)

    label_subtest4 = Label(frame_subtest4, text="Виберіть формулу дискримінанта")
    label_subtest4.pack(side=TOP, padx=5, pady=5)

    label_showtest4 = Label(sub4, text="")
    label_showtest4.pack(side=BOTTOM, padx=5, pady=5)

    frame_answertest4 = Frame(sub4)
    frame_answertest4.pack(fill=X)

    if not used_test4:
        button_answertest4_correct = Button(frame_answertest4, text="D=b²-4ac", command=lambda: answer_test4(True, label_showtest4, sub4))
        button_answertest4_correct.pack(side=TOP, padx=5, pady=5)

        button_answertest4_incorrect = Button(frame_answertest4, text="C₆H₁₂O₆", command=lambda: answer_test4(False, label_showtest4, sub4))
        button_answertest4_incorrect.pack(side=TOP, padx=5, pady=5)

def answer_test4(correct, label, window):
    global used_test4, result, tests_passed
    used_test4 = True
    tests_passed += 1
    if correct:
        result += 1
        label["text"] = "Відповідь вірна"
    else:
        label["text"] = "Відповідь не вірна"
    update_labels()  # Оновлюємо лейбли
    window.after(2000, window.destroy)  # Закриття вікна через 2 секунди

def test5():
    global used_test5
    sub5 = Tk()
    sub5.title("Test5")
    sub5.geometry("300x200")
    sub5.resizable(width=False, height=False)

    frame_subtest5 = Frame(sub5)
    frame_subtest5.pack(fill=X)

    label_subtest5 = Label(frame_subtest5, text="Чи подобається вам програмування?")
    label_subtest5.pack(side=TOP, padx=5, pady=5)

    label_showtest5 = Label(sub5, text="")
    label_showtest5.pack(side=BOTTOM, padx=5, pady=5)

    frame_answertest5 = Frame(sub5)
    frame_answertest5.pack(fill=X)

    if not used_test5:
        button_answertest5_yes = Button(frame_answertest5, text="Так", command=lambda: answer_test5(True, label_showtest5, sub5))
        button_answertest5_yes.pack(side=LEFT, padx=5, pady=5)

        button_answertest5_no = Button(frame_answertest5, text="Ні", command=lambda: answer_test5(False, label_showtest5, sub5))
        button_answertest5_no.pack(side=RIGHT, padx=5, pady=5)

def answer_test5(correct, label, window):
    global used_test5, result, tests_passed
    used_test5 = True
    tests_passed += 1
    if correct:
        result += 1
        label["text"] = "Відповідь вірна"
    else:
        label["text"] = "Відповідь не вірна"
    update_labels()  # Оновлюємо лейбли
    window.after(2000, window.destroy)  # Закриття вікна через 2 секунди


# Основне вікно для вибору завдання
frame_main = Frame(root)
frame_main.pack(fill=X)

label_main = Label(frame_main, text="Меню вибору завдань")
label_main.grid(row=0, column=1, pady=10)

# Перший тест
label_test1 = Label(frame_main, text="Перший Тест - ")
label_test1.grid(row=1, column=0, padx=10, pady=10)

button_test1 = Button(frame_main, text="Тест 1", command=test1)
button_test1.grid(row=1, column=1, padx=10, pady=10)

# Другий тест
label_test2 = Label(frame_main, text="Другий Тест - ")
label_test2.grid(row=2, column=0, padx=10, pady=10)

button_test2 = Button(frame_main, text="Тест 2", command=test2)
button_test2.grid(row=2, column=1, padx=10, pady=10)

# Третій тест
label_test3 = Label(frame_main, text="Третій тест - ")
label_test3.grid(row=3, column=0, padx=10, pady=10)

button_test3 = Button(frame_main, text="Тест 3", command=test3)
button_test3.grid(row=3, column=1, padx=10, pady=10)

# Четвертий тест
label_test4 = Label(frame_main, text="Четвертий тест - ")
label_test4.grid(row=4, column=0, padx=10, pady=10)

button_test4 = Button(frame_main, text="Тест 4", command=test4)
button_test4.grid(row=4, column=1, padx=10, pady=10)

# П'ятий тест
label_test5 = Label(frame_main, text="П'ятий тест - ")
label_test5.grid(row=5, column=0, padx=10, pady=10)

button_test5 = Button(frame_main, text="Тест 5", command=test5)
button_test5.grid(row=5, column=1, padx=10, pady=10)

label_final = Label(root, text="Пройдено тестів 0/5")
label_final.pack(side=BOTTOM, padx=5, pady=5)

label_score = Label(root, text="Балів - 0/10")
label_score.pack(side=BOTTOM, padx=5, pady=5)
# Створення змінних для діалогового вікна
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()

root.mainloop()




