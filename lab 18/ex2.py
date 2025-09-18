import math as m
import numpy as np

start_def = 0
stop_def = 1
step_def = 0.1

def get_valid_float_input(prompt, default):
    while True:
        value = input(prompt)
        if value.strip() == "":
            print(f"Використано значення за замовчуванням: {default}")
            return default
        try:
            return float(value)
        except ValueError:
            print(" Некоректне значення. Спробуйте ще раз.")

start = get_valid_float_input("Введіть початок відліку (start) або лишіть рядок пустим: ", start_def)
stop = get_valid_float_input("Введіть кінець відліку (stop) або лишіть рядок пустим: ", stop_def)
step = get_valid_float_input("Введіть крок (step) або лишіть рядок пустим: ", step_def)


if step == 0:
    print(" Крок не може бути нульовим.")
    exit()

print("Результати обчислень:")
print(f"{'i':>8} | {'f1':>12} | {'f2':>12}")
print("-" * 36)

for i in np.arange(start, stop, step):
    try:
        expr = m.cos(i ** 2 - 2 ** -i)
        f1 = m.sin(expr)
        f2 = m.tan(expr ** 2)

        print(f"{i:8.4f} | {f1:12.6f} | {f2:12.6f}")
    except Exception as e:
        print(f"{i:8.4f} | Помилка: {e}")

