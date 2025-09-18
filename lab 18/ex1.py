import math

x_def = 1.5
y_def = 0.1
z_def = 0.5

def corect_input(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print(" Некоректне значення. Спробуйте ще раз.")


print("Ви можете ввести свої значення для x, y, z або використати значення за замовчуванням.")
choice = input("Хочете використати значення за замовчуванням? (так / ні): ").strip().lower()

if choice in ["так", "т", "yes", "y"]:
    x = x_def
    y = y_def
    z = z_def
    print(f"\n✅ Використовуються значення за замовчуванням: x={x}, y={y}, z={z}")
else:
    x = corect_input("Введіть число x: ")
    y = corect_input("Введіть число y: ")
    z = corect_input("Введіть число z: ")

def expr(n1, n2, g):
    return abs(g) + n1 * math.tan(n2)

term1 = 87 / expr(x, y, z)
term2 = expr(2, y, z) / 34
term3 = 7.54 / expr(1, 1.3, z)
S = term1 + term2 + term3

result =  S
print(f"\n✅ Результат обчислення S: {result:.4f}")
