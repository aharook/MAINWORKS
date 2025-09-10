def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):  # перевіряємо тільки до √x
        if x % i == 0:
            return False
    return True


def find_twins(n):
    for k in range(n, 2*n - 1):  # до 2n-1, бо беремо пари (k, k+2)
        if is_prime(k) and is_prime(k + 2):
            return (k, k + 2)   # повертаємо першу знайдену пару
    return None



n = int(input("Введіть n: "))

pair = find_twins(n)
if pair:
    print(f"Знайдено прості близнята: {pair[0]} і {pair[1]}")
else:
    print("Серед чисел від n до 2n простих близнят нема.")
