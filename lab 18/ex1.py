import math

x_def = 1.5
y_def = 0.1
z_def = 0.5


def correct_input(value, default):
    try:
        value = float(value)  
        return value
    except ValueError:
        print(f"Некоректне значення. Використовується значення за замовчуванням: {default}")
        return default
    

x = input("Введіть число x: ")
x = correct_input(x, x_def)
y = input("Введіть число y: ")
y = correct_input(y, y_def)
z = input("Введіть число z: ")
z = correct_input(z, z_def)

S = (87 / abs(math.log10(abs(1)) + x * math.tan(y))) + \
    (abs(math.log10(abs(1)) + 2 * math.tan(y)) / 34) + \
    (7.54 / abs(math.log10(abs(1)) + math.tan(1.3)))
    
print(f"Результат обчислення S: {S:.4f}")
