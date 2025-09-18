class AnalizText():
    def correct_input(self):
        text = input("Введіть рядок: ").lower()
        while not text:
            print("Рядок не може бути порожнім. Спробуйте ще раз.")
            text = input("Введіть рядок: ").lower()
        count_p = text.count('п')
        count_r = text.count('р')
    
        if count_p == 0 :
            print("Букв 'п' немає.")
        if count_r == 0 :
            print("Букв 'р' немає.")

        if count_p > count_r:
            print("Букв 'п' більше, ніж 'р'.")
        elif count_p < count_r:
            print("Букв 'п' не більше, ніж 'р'.")
        elif count_p == count_r:
            print("Кількість букв 'п' і 'р' однакова.")
        


class CorrectInput():
    pass