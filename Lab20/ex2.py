import os

filename = r"D:\MAINWORKS\Lab20\names.txt"  

if not os.path.exists(filename):
    print(f"Помилка: файл {filename} не існує!")
else:
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()

    print("Вміст файлу:\n")
    print(data)
