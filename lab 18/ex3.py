def binary_search(arr, target):
    """Бінарний пошук. Повертає індекс або -1, якщо не знайдено."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


try:
    n = int(input("Введіть кількість елементів масиву: "))
    if n <= 0:
        raise ValueError("Кількість елементів повинна бути додатною.")
except ValueError:
    print("Некоректне значення введіть ціле додатне число.")
    exit()
arr = []

is_sorted = True

for i in range(n):
    try:
        x = int(input(f"Елемент {i+1}: "))
    except ValueError:
        print("Некоректне значення. Введіть ціле число.")
        exit()
    arr.append(x)
    if i > 0 and arr[i] < arr[i - 1]:
        is_sorted = False

if not is_sorted:
    print("Масив не відсортований. Бінарний пошук неможливий.")
else:
    target = int(input("Введіть число для пошуку: "))
    result = binary_search(arr, target)
    if result != -1:
        print(f"Число {target} знайдено на позиції {result} (індексація з нуля).")
    else:
        print(f"Число {target} не знайдено у масиві.")


