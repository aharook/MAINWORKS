import numpy as np
a=8
b=50
N = int(input("Введіть N: "))
randomNumbers = np.random.randint(a, b, N)
new_randomNumbers = []
print("Основні 10 значень масиву:")
for i in range(N):
    print(f"За індексом {i}, номер: {randomNumbers[i]}")
np.sum(randomNumbers)
print("Сума всіх елементів масиву:", np.sum(randomNumbers))
print("бажаєте вивести 4 нових значення? (y/n)")
answer = input()
if answer == "y":
    for i in range(4):
        new_randomNumbers.append(np.random.randint(a, b))
        print(f"за індексом: {i + N}, номер: {new_randomNumbers[i]}")
elif answer == "n":
    print("Дякую за увагу!")
else:
    while answer != "y" and answer != "n":
        answer = input("Введіть y або n\n")
    
    if answer == "y":
        for i in range(4):
            new_randomNumbers.append(np.random.randint(a, b))
            print(f"за індексом: {i + N}, номер: {new_randomNumbers[i]}")
    else:
        print("Дякую за увагу!")
