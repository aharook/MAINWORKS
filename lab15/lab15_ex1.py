import numpy as np

m = int(input("Введіть кількість рядків (M): "))
n = int(input("Введіть кількість стовпців (N): "))

array = np.random.uniform(size=(m, n))
print("Масив:")
print(array)

total = np.sum(array)
print("Сума елементів:", total)
