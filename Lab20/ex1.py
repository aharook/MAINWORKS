
writers = []

for i in range(5):
    name = input(f"Введіть прізвище письменника {i+1}: ")
    writers.append(name)

filename = r"D:\MAINWORKS\Lab20\names.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write("\n".join(writers))

print("Файл успішно створено та записано:", filename)


flash_path = r"E:\Harchuk.txt" 

try:
    with open(filename, "r", encoding="utf-8") as src:
        data = src.read()
    with open(flash_path, "w", encoding="utf-8") as dst:
        dst.write(data)
    print("Файл скопійовано на флешку:", flash_path)
except FileNotFoundError:
    print("Помилка: не знайдено флешку або шлях неправильний.")

        
