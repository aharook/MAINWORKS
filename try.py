import math as mt

class dicipline:
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours
        self.grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 1 and 5")

    def set_name(self, name):
        self.name = name
    def set_hours(self, hours):
        self.hours = hours
    def set_grades(self, grades):
        self.grades = grades
    def get_name(self):
        return self.name
    def get_hours(self):
        return self.hours
    def get_grades(self):
        return self.grades
    
    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def __str__(self):
        return f"Дисципліна: {self.name}, Години {self.hours}, Оцінки {self.grades}, Середня оцінка {self.average_grade():.2f}"

class statistician:
    def __init__(self):
        self.disciplines = []

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)

    def overall_average(self):
        if not self.disciplines:
            return 0
        total = sum(d.average_grade() for d in self.disciplines)
        return total / len(self.disciplines)
    
    def baddest_discipline(self):
        if not self.disciplines:
            return None
        best = max(self.disciplines, key=lambda d: d.average_grade())
        return best
    def worst_discipline(self):
        if not self.disciplines:
            return None
        worst = min(self.disciplines, key=lambda d: d.average_grade())
        return worst
    
    def __str__(self):
        result = "Статистика дисциплін:\n"
        for d in self.disciplines:
            result += str(d) + "\n"
        result += f"Загальна середня оцінка: {self.overall_average():.2f}"
        return result

def save_to_file(stat):
    with open("disciplines.txt", "w", encoding="utf-8") as f:
        for d in stat.disciplines:
            grades = ",".join(map(str, d.grades))
            f.write(f"{d.name}|{d.hours}|{grades}\n")
    print("Дані збережено у файл disciplines.txt")

def load_from_file(stat):
    try:
        with open("disciplines.txt", "r", encoding="utf-8") as f:
            for line in f:
                name, hours, grades = line.strip().split("|")
                disc = dicipline(name, int(hours))

                if grades:
                    for g in grades.split(","):
                        disc.add_grade(int(g))

                stat.add_discipline(disc)

        print("Дані успішно завантажено з файлу.")
    except FileNotFoundError:
        print("Файл не знайдено. Спочатку збережіть дані.")
    except Exception as e:
        print("Помилка читання файлу:", e)



if __name__ == "__main__":
    stat = statistician()
    load_from_file(stat)

    while True:
        print("\n====== М Е Н Ю ======")
        print("1. Додати дисципліну")
        print("2. Показати всі дисципліни")
        print("3. Показати дисципліну з найвищою середньою оцінкою")
        print("4. Показати дисципліну з найнижчою середньою оцінкою")
        print("5. Показати загальну середню оцінку")
        print("6. Зберегти у файл")
        print("7. Завантажити з файлу")
        print("0. Вихід")

        choice = input("Введіть номер операції: ")

        match choice:
            case "1":
                name = input("Введіть назву дисципліни: ")
                hours = int(input("Введіть кількість годин: "))
                disc = dicipline(name, hours)

                grade_count = int(input("Введіть кількість оцінок: "))
                for _ in range(grade_count):
                    grade = int(input("Введіть оцінку (1-5): "))
                    disc.add_grade(grade)

                stat.add_discipline(disc)
                print("Дисципліну додано!")

            case "2":
                print("\n=== Усі дисципліни ===")
                print(stat)

            case "3":
                best = stat.baddest_discipline()
                print(best if best else "Немає дисциплін.")

            case "4":
                worst = stat.worst_discipline()
                print(worst if worst else "Немає дисциплін.")

            case "5":
                print(f"Загальна середня оцінка: {stat.overall_average():.2f}")

            case "6":
                save_to_file(stat)

            case "7":
                stat.disciplines.clear()   # щоб не дублювались
                load_from_file(stat)

            case "0":
                print("Вихід...")
                break

            case _:
                print("Некоректний вибір.")

