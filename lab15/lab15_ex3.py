import numpy as np

def get_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            else:
                print("Число повинно бути більше нуля.")
        except ValueError:
            print("Некоректне значення. Введіть ціле число.")

print("Введення розмірів матриць для множення:")
rows_a = get_positive_int("Кількість рядків першої матриці: ")
cols_a = get_positive_int("Кількість стовпців першої матриці (і рядків другої): ")
cols_b = get_positive_int("Кількість стовпців другої матриці: ")

matrix_a = np.random.uniform(0, 10, size=(rows_a, cols_a))
matrix_b = np.random.uniform(0, 10, size=(cols_a, cols_b))
result = np.dot(matrix_a, matrix_b)

print("\nПерша матриця A:")
for row in matrix_a:
    print(' '.join(f"{num:.2f}" for num in row))

print("\nДруга матриця B:")
for row in matrix_b:
    print(' '.join(f"{num:.2f}" for num in row))

print("\nРезультат множення A * B:")
for row in result:
    print(' '.join(f"{num:.2f}" for num in row))
