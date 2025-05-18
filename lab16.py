text = input("Введіть рядок: ").lower()

count_p = text.count('п')
count_r = text.count('р')

if count_p > count_r:
    print("Букв 'п' більше, ніж 'р'.")
elif count_p == count_r:
    print("Кількість букв 'п' та 'р' однакова.")
else:
    print("Букв 'п' менше ніж 'р'.")

print(f"Кількість 'п': {count_p}, кількість 'р': {count_r}.")