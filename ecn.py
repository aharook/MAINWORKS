import math

# Значення за замовчуванням
x_def = 1.5
y_def = 0.1
z_def = 0.5

# Безпечне введення чисел
def get_valid_float(prompt, default):
    while True:
        value = input(prompt)
        if value.strip() == "":
            print(f"✅ Використовується значення за замовчуванням: {default}")
            return default
        try:
            return float(value)
        except ValueError:
            print("❌ Некоректне значення. Спробуйте ще раз.")

# Загальна функція виразу (abs(g) + n1 * tan(n2))
def custom_expr(n1, n2, g):
    return abs(g) + n1 * math.tan(n2)

# --- Основна програма ---
choice = input("Хочете використати значення за замовчуванням? (так / ні): ").strip().lower()

if choice in ["так", "т", "yes", "y"]:
    x = x_def
    y = y_def
    z = z_def
    print(f"\n✅ Використовуються значення за замовчуванням: x={x}, y={y}, z={z}")
else:
    x = get_valid_float("Введіть число x: ", x_def)
    y = get_valid_float("Введіть число y: ", y_def)
    z = get_valid_float("Введіть число z: ", z_def)

# Розрахунок доданків
denominator1 = custom_expr(x, y, z)
term1 = 87 / denominator1

denominator2 = custom_expr(2, y, z)
term2 = denominator2 / 34

denominator3 = custom_expr(1, 1.3, z)
term3 = 7.54 / denominator3

# Вивід результатів
print(f"\n🔹 Перший доданок: {term1:.4f}")
print(f"🔹 Другий доданок: {term2:.4f}")
print(f"🔹 Третій доданок: {term3:.4f}")

S = term1 + term2 + term3
print(f"\n✅ Результат обчислення S: {S:.4f}")
