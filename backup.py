import numpy as np
a = int(input("Введіть початок діапазону: "))
b = int(input("Введіть кінець діапазону: "))
c = input("Введіть число, яке буде додано до суми елементів масиву: ")
randomNumbers = np.random.randint(a, b, 10)
print("Основні 10 значень масиву:")
for i in range(10):
    print(f"Index: {i}, Number: {randomNumbers[i]}")
np.sum(randomNumbers )
sumc = np.sum(randomNumbers)+ int(c)
print("Сума всіх елементів масиву:", np.sum(randomNumbers), "сума з додаванням с: ",sumc)