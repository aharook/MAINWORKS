import numpy as np
a=8
b=50
randomNumbers = np.random.randint(a, b, 10)
print("Основні 10 значень масиву:")
for i in range(10):
    print(f"Index: {i}, Number: {randomNumbers[i]}")
np.sum(randomNumbers)
print("Сума всіх елементів масиву:", np.sum(randomNumbers))