class AnalizText():
    def correct_input(self):
        try:
            text = str(text)  
        except ValueError:
            print(f"Некоректне значення. Введіть текстовий рядок.")
            return None
        text = input("Введіть рядок: ").lower()

        count_p = text.count('п')
        count_r = text.count('р')

        if count_p > count_r:
            print("Букв 'п' більше, ніж 'р'.")
        else:
            print("Букв 'п' не більше, ніж 'р'.")

class CorrectInput():
    pass