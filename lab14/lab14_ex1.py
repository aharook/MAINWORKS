import random
import time

a = 8.0
b = 50.0
randomNumbers = []
size = 20000

def boobliksort(arr):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False  
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    print("Відсортовані числа:", arr)

def insertionSort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    print("Відсортовані числа:", arr)

def selectionSort(arr, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if arr[i] < arr[min_idx]:
                min_idx = i
        arr[step], arr[min_idx] = arr[min_idx], arr[step]
    print("Відсортовані числа:", arr)

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quickSort(left) + [pivot] + quickSort(right)

for _ in range(size):
    number = round(random.uniform(a, b), 2)
    randomNumbers.append(number)

print("Оберіть метод сортування:")
print("1. Бульбашкою")
print("2. Вставками")
print("3. Вибором")
print("4. Вбудоване сортування (sorted)")
print("5. Швидке сортування (quickSort)")

choice = int(input("Введіть номер методу: "))

start_time = time.time()

if choice == 1:
    print("Сортування бульбашкою:")
    boobliksort(randomNumbers)
elif choice == 2:
    print("Сортування вставками:")
    insertionSort(randomNumbers)
elif choice == 3:
    print("Сортування вибором:")
    selectionSort(randomNumbers, size)
elif choice == 4:
    print("Вбудоване сортування:")
    sortedNumbers = sorted(randomNumbers)
    print("Відсортовані числа:", sortedNumbers)
elif choice == 5:
    print("Швидке сортування:")
    sortedNumbers = quickSort(randomNumbers)
    print("Відсортовані числа:", sortedNumbers)
else:
    print("Невірний вибір!")
    exit()

end_time = time.time()
print(f"\nЧас виконання: {end_time - start_time:.4f} секунд")



