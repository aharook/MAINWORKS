import numpy as np

ROWS = 5
COLS = 5

elements = []
print("Введіть елементи матриці 5x5 (по рядках):")
for i in range(ROWS):
    for j in range(COLS):
        while True:
            try:
                val = float(input(f"Елемент [{i+1}][{j+1}]: "))
                elements.append(val)
                break
            except ValueError:
                print("Некоректне значення. Введіть число.")

matrix = np.array(elements).reshape((ROWS, COLS))

while True:
    try:
        k = int(input("Введіть номер рядка K (1-5): "))
        if 1 <= k <= 5:
            break
        else:
            print("K повинно бути в межах від 1 до 5.")
    except ValueError:
        print("Некоректне значення. Введіть ціле число.")

k_index = k - 1
diag_element = matrix[k_index][k_index]

if diag_element == 0:
    print("Діагональний елемент дорівнює нулю. Ділення неможливе.")
else:
    matrix[k_index] = matrix[k_index] / diag_element

print("Оновлена матриця:")
for row in matrix:
    print(' '.join(f"{num:.2f}" for num in row))

