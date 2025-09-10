import math as m
import numpy as np

start_def = 0
stop_def = 1
step_def = 0.1
f1 = 0
f2 = 0 



def correct_input(value, default):
    try:
        value = float(value)  
        return value
    except ValueError:
        print(f"Некоректне значення. Використовується значення за замовчуванням: {default}")
        return default  

start = input("Введіть початок відліку або лишіть рядок пустим щоб використати значення дефолту: ")
start = correct_input(start, start_def)
stop = input("Введіть кінець відліку  або лишіть рядок пустим щоб використати значення дефолту: ")
stop = correct_input(stop, stop_def)
step = input("Введіть крок  або лишіть рядок пустим щоб використати значення дефолту: ")
step = correct_input(step, step_def)


for i in np.arange(start, stop, step):
    f1 = m.sin(m.cos(pow(start, 2) - pow(2, -start )))


for i in np.arange(start, stop, step):
    f2 = m.tan(pow(m.cos(pow(start, 2) - pow(2, -start )),2))

print(f"Результат обчислення f1: {f1:.4f}")
print(f"Результат обчислення f2: {f2:.4f}")


