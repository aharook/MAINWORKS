import numpy as np

money = 1000
HP = 100
radiation = 0
hungruy = 0
armor = 0


artifacts = [
    {
        "name": "КРОВ КАМЕНЮ",
        "description": "Поступово відновлює здоров'я.",
        "effects": {"HP": +10},
        "price": 150
    },
    {
        "name": "ДУША",
        "description": "Зменшує радіацію.",
        "effects": {"radiation": -5},
        "price": 250
    }
]

inventory_artifacts = [{
        "name": "КРОВ КАМЕНЮ",
        "description": "Поступово відновлює здоров'я.",
        "effects": {"HP": +10},
        "price": 150
    },
    {
        "name": "ДУША",
        "description": "Зменшує радіацію.",
        "effects": {"radiation": -5},
        "price": 250
    }]


def statistick():
    print("\n============== СТАТИСТИКА ==============")
    print("💰 Гроші:        " + str(money) + "₴")
    print("❤️ Здоров'я:      " + str(HP) + "%")
    print("☢ Радіація:       " + str(radiation) + "%")
    print("🍖 Голод:         " + str(hungruy) + "%")
    print("🛡️ Броня:         " + str(armor) + "%")
    print("========================================")

def show_artifacts():
    if not inventory_artifacts:
        print("\n⚠️ У вас немає артефактів.")
    else:
        print("\n=========== АРТЕФАКТИ ===========")
        for i, art in enumerate(inventory_artifacts):
            print(f"💠 {i+1}. {art['name']} — {art['description']}")
        print("================================")
        print("[1] 📥 Використати")
        print("[2] ❌ Не використовувати")
        use = int(input(">>> Ваш вибір: "))
        if use == 1:
            index = int(input("Оберіть номер артефакта: ")) - 1
            use_artifact(index)
        elif use == 2:
            print("Ви вирішили не використовувати артефакт.")
        else:
            print("❗ Невірний вибір!")


def use_artifact(index):
    global HP, radiation
    if 0 <= index < len(inventory_artifacts):
        art = inventory_artifacts[index]
        HP = min(100, HP + art["effects"].get("HP", 0))
        radiation = max(0, radiation + art["effects"].get("radiation", 0))
        print(f"\nВикористано {art['name']}.\n")
        del inventory_artifacts[index]
    else:
        print("❗ Невірний номер артефакту.")


def menu():
    print("\n============== МЕНЮ ==============")
    print("[1] 📦 Інвентар")
    print("[2] 🧍 Статистика")
    print("[3] ☢ Артефакти")
    print("[4] ❌ Вийти з гри")
    print("==================================")
    menu_use = int(input(">>> Оберіть дію: "))
    if menu_use == 1:
        invenory()
    elif menu_use == 2:
        statistick()
    elif menu_use == 3:
        show_artifacts()
    elif menu_use == 4:
        print("❗ Ви вийшли з гри.")
        exit()
    else:
        print("❗ Невірний вибір!")
        exit()


def invenory():
    global HP
    print("\n============== ІНВЕНТАР ==============")
    inventory = np.array(["Пістолет", "Граната", "Аптечка"])
    for i in range(len(inventory)):
        print(f"[{i + 1}] {inventory[i]}")
    print("[4] 🚪 Вийти з інвентарю")
    print("=====================================")
    inventory_use = int(input(">>> Оберіть предмет: "))
    if inventory_use == 1:
        print("Ви вибрали пістолет. Патронів: 0/10")
    elif inventory_use == 2:
        print("Ви вибрали гранату.")
    elif inventory_use == 3:
        print("Ви вибрали аптечку. Використати аптечку?")
        print("[1] 🩹 Так\n[2] ❌ Ні")
        use = int(input(">>> Ваш вибір: "))
        if use == 1:
            HP = min(100, HP + 20)
            print(f"Ви використали аптечку. Здоров'я: {HP}%")
        elif use == 2:
            print("Ви не використали аптечку.")
        else:
            print("❗ Невірний вибір!")
    elif inventory_use == 4:
        print("🚪 Ви вийшли з інвентарю.")
    else:
        print("❗ Невірний вибір!")
        exit()


def Sidor():
    print("\n―――――――――――――――――――――――――――――")
    print("🧔 СИДОРОВИЧ:\n  \"Знову ти? Маю дещо цікаве...\"")
    print("―――――――――――――――――――――――――――――")
    print("[1] 💎 Купити артефакт")
    print("[2] 🔫 Придбати зброю")
    print("[3] 🚪 Вийти з магазину")
    Sidor_use = int(input(">>> Ваш вибір: "))
    if Sidor_use == 1:
        print("\nДоступні артефакти:")
        for i, art in enumerate(artifacts):
            print(f"💠 {i+1}. {art['name']} — {art['price']}₴: {art['description']}")
        choice = int(input("Оберіть артефакт: ")) - 1
        if 0 <= choice < len(artifacts):
            inventory_artifacts.append(artifacts[choice])
            print(f"Ви купили {artifacts[choice]['name']}.")
        else:
            print("❗ Невірний вибір!")
    elif Sidor_use == 2:
        print("🔫 Ви купили зброю.")
    elif Sidor_use == 3:
        print("🚪 Ви вийшли з магазину.")
    else:
        print("❗ Невірний вибір!")
        exit()


def Selo():
    print("\n🌫️ Ви знаходитеся в селі Новачків...")
    print("Навколо — тиша, тріщить гейґер...")
    print("--------------------------------------")
    print("[1] 🔍 Оглянути місцевість")
    print("[2] 🗣️ Поговорити з місцевими")
    print("[3] ☢ Увійти в Зону (WIP)")
    print("[4] 🧔 Зайти до Сидоровича")
    print("[5] 🛠️ Відкрити меню")
    print("--------------------------------------")
    Selo_use = int(input(">>> Оберіть дію: "))
    if Selo_use == 1:
        print("🔍 Навколо сиро і холодно.")
    elif Selo_use == 2:
        print("🗣️ Місцеві розповіли вам про Зону.")
    elif Selo_use == 4:
        Sidor()
    elif Selo_use == 5:
        menu()
    else:
        print("❗ Невірний вибір!")
        exit()


print("🎮 Вітаю в Зоні Відчуження!")
print("[1] 🏁 Розпочати нову гру")
print("[2] 💾 Завантажити гру (не реалізовано)")
print("[3] ❌ Вихід")
action = int(input(">>> Введіть номер дії: "))
if action == 1:
    name = input("Введіть ім'я персонажа: ")
    print(f"🎉 Вітаю, {name}!")
    menu()
elif action == 2:
    print("💾 Завантаження гри ще не реалізовано.")
    exit()
elif action == 3:
    print("❌ Вихід з гри.")
    exit()
else:
    print("❗ Невірний вибір!")
    exit()

print("⏳ Час рухатися далі...")
Selo()
import numpy as np


HP = 100
radiation = 0
hungruy = 0
armor = 0


artifacts = [
    {
        "name": "КРОВ КАМЕНЮ",
        "description": "Поступово відновлює здоров'я.",
        "effects": {"HP": +10},
        "price": 150
    },
    {
        "name": "ДУША",
        "description": "Зменшує радіацію.",
        "effects": {"radiation": -5},
        "price": 250
    }
]

inventory_artifacts = []


def statistick():
    print("\n============== СТАТИСТИКА ==============")
    print("❤️ Здоров'я:      " + str(HP) + "%")
    print("☢ Радіація:       " + str(radiation) + "%")
    print("🍖 Голод:         " + str(hungruy) + "%")
    print("🛡️ Броня:         " + str(armor) + "%")
    print("========================================")


def show_artifacts():
    if not inventory_artifacts:
        print("\n⚠️ У вас немає артефактів.")
    else:
        print("\n=========== АРТЕФАКТИ ===========")
        for i, art in enumerate(inventory_artifacts):
            print(f"💠 {i+1}. {art['name']} — {art['description']}")
        print("================================")
        print("[1] 📥 Використати")
        print("[2] ❌ Не використовувати")
        use = int(input(">>> Ваш вибір: "))
        if use == 1:
            index = int(input("Оберіть номер артефакта: ")) - 1
            use_artifact(index)
        elif use == 2:
            print("Ви вирішили не використовувати артефакт.")
        else:
            print("❗ Невірний вибір!")


def use_artifact(index):
    global HP, radiation
    if 0 <= index < len(inventory_artifacts):
        art = inventory_artifacts[index]
        HP = min(100, HP + art["effects"].get("HP", 0))
        radiation = max(0, radiation + art["effects"].get("radiation", 0))
        print(f"\nВикористано {art['name']}.\n")
        del inventory_artifacts[index]
    else:
        print("❗ Невірний номер артефакту.")


def menu():
    print("\n============== МЕНЮ ==============")
    print("[1] 📦 Інвентар")
    print("[2] 🧍 Статистика")
    print("[3] ☢ Артефакти")
    print("[4] ❌ Вийти з гри")
    print("==================================")
    menu_use = int(input(">>> Оберіть дію: "))
    if menu_use == 1:
        invenory()
    elif menu_use == 2:
        statistick()
    elif menu_use == 3:
        show_artifacts()
    elif menu_use == 4:
        print("❗ Ви вийшли з гри.")
        exit()
    else:
        print("❗ Невірний вибір!")
        exit()


def invenory():
    global HP
    print("\n============== ІНВЕНТАР ==============")
    inventory = np.array(["Пістолет", "Граната", "Аптечка"])
    for i in range(len(inventory)):
        print(f"[{i + 1}] {inventory[i]}")
    print("[4] 🚪 Вийти з інвентарю")
    print("=====================================")
    inventory_use = int(input(">>> Оберіть предмет: "))
    if inventory_use == 1:
        print("Ви вибрали пістолет. Патронів: 0/10")
    elif inventory_use == 2:
        print("Ви вибрали гранату.")
    elif inventory_use == 3:
        print("Ви вибрали аптечку. Використати аптечку?")
        print("[1] 🩹 Так\n[2] ❌ Ні")
        use = int(input(">>> Ваш вибір: "))
        if use == 1:
            HP = min(100, HP + 20)
            print(f"Ви використали аптечку. Здоров'я: {HP}%")
        elif use == 2:
            print("Ви не використали аптечку.")
        else:
            print("❗ Невірний вибір!")
    elif inventory_use == 4:
        print("🚪 Ви вийшли з інвентарю.")
    else:
        print("❗ Невірний вибір!")
        exit()


def Sidor():
    print("\n―――――――――――――――――――――――――――――")
    print("🧔 СИДОРОВИЧ:\n  \"Знову ти? Маю дещо цікаве...\"")
    print("―――――――――――――――――――――――――――――")
    print("[1] 💎 Купити артефакт")
    print("[2] 🔫 Придбати зброю")
    print("[3] 🚪 Вийти з магазину")
    Sidor_use = int(input(">>> Ваш вибір: "))
    if Sidor_use == 1:
        print("\nДоступні артефакти:")
        for i, art in enumerate(artifacts):
            print(f"💠 {i+1}. {art['name']} — {art['price']}₴: {art['description']}")
        choice = int(input("Оберіть артефакт: ")) - 1
        if 0 <= choice < len(artifacts):
            inventory_artifacts.append(artifacts[choice])
            print(f"Ви купили {artifacts[choice]['name']}.")
        else:
            print("❗ Невірний вибір!")
    elif Sidor_use == 2:
        print("🔫 Ви купили зброю.")
    elif Sidor_use == 3:
        print("🚪 Ви вийшли з магазину.")
    else:
        print("❗ Невірний вибір!")
        exit()


def Selo():
    global HP, radiation, hungruy, armor
    while True:  # Додаємо цикл, щоб користувач міг продовжувати вибір
        print("\n🌫️ Ви знаходитеся в селі Новачків...")
        print("Навколо — тиша, тріщить гейґер...")
        print("--------------------------------------")
        print("[1] 🔍 Оглянути місцевість")
        print("[2] 🗣️ Поговорити з місцевими")
        print("[3] ☢ Увійти в Зону (WIP)")
        print("[4] 🧔 Зайти до Сидоровича")
        print("[5] 🛠️ Відкрити меню")
        print("--------------------------------------")
        
        Selo_use = int(input(">>> Оберіть дію: "))
        
        if Selo_use == 1:
            print("🔍 Навколо сиро і холодно.")
            continue
        elif Selo_use == 2:
            print("🗣️ Місцеві розповіли вам про Зону.")
            continue
        elif Selo_use == 4:
            Sidor()  # Перехід до магазину Сидоровича
        elif Selo_use == 5:
            menu()  # Перехід до головного меню
            return
        else:
            print("❗ Невірний вибір! Спробуйте ще раз.")


if __name__ == "__main__":
   def main():
        print("🎮 Вітаю в Зоні Відчуження!")
        print("[1] 🏁 Розпочати нову гру")
        print("[2] 💾 Завантажити гру (не реалізовано)")
        print("[3] ❌ Вихід")
        action = int(input(">>> Введіть номер дії: "))
        if action == 1:
            name = input("Введіть ім'я персонажа: ")
            print(f"🎉 Вітаю, {name}!")
            menu()
        elif action == 2:
            print("💾 Завантаження гри ще не реалізовано.")
            exit()
        elif action == 3:
            print("❌ Вихід з гри.")
            exit()
        else:
            print("❗ Невірний вибір!")
            exit()
        print("⏳ Час рухатися далі...")
        print("\n🌫️ Ви знаходитеся в селі Новачків...")
        print("Навколо — тиша, тріщить гейґер...")
        Selo()
