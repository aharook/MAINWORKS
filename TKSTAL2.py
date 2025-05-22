import tkinter as tk
from tkinter import messagebox

# Стани гри
money = 1000
HP = 100
radiation = 0
hungruy = 0
armor = 0

artifacts = [
    {"name": "КРОВ КАМЕНЮ", "description": "Поступово відновлює здоров'я.", "effects": {"HP": 10}, "price": 150},
    {"name": "ДУША", "description": "Зменшує радіацію.", "effects": {"radiation": -5}, "price": 250}
]
inventory_artifacts = []

def update_stats():
    stats.config(text=f"❤️ Здоров'я: {HP}%   ☢ Радіація: {radiation}%   🍖 Голод: {hungruy}%   🛡 Броня: {armor}%   💰 Гроші: {money}₴")

def use_artifact(index):
    global HP, radiation
    if 0 <= index < len(inventory_artifacts):
        art = inventory_artifacts.pop(index)
        HP = min(100, HP + art["effects"].get("HP", 0))
        radiation = max(0, radiation + art["effects"].get("radiation", 0))
        update_stats()
        messagebox.showinfo("Успіх", f"Використано артефакт: {art['name']}")
        show_artifacts()
    else:
        messagebox.showerror("Помилка", "Невірний індекс артефакту")

def show_artifacts():
    win = tk.Toplevel(root)
    win.title("Артефакти")
    win.geometry("400x300")
    if not inventory_artifacts:
        tk.Label(win, text="⚠️ У вас немає артефактів", font=("Arial", 12)).pack(pady=20)
        return
    for i, art in enumerate(inventory_artifacts):
        btn = tk.Button(win, text=f"{i+1}. {art['name']} — {art['description']}", font=("Arial", 11),
                        command=lambda i=i: use_artifact(i))
        btn.pack(fill='x', padx=10, pady=5)

def inventory_window():
    win = tk.Toplevel(root)
    win.title("Інвентар")
    win.geometry("400x250")
    items = ["Пістолет", "Граната", "Аптечка"]

    for item in items:
        tk.Label(win, text=item, font=("Arial", 12)).pack(pady=2)

    def heal():
        global HP
        HP = min(100, HP + 20)
        update_stats()
        messagebox.showinfo("Аптечка", "Ви використали аптечку.")

    tk.Button(win, text="🩹 Використати аптечку", command=heal, font=("Arial", 12), bg="#28a745", fg="white").pack(pady=10)

def shop():
    win = tk.Toplevel(root)
    win.title("Сидорович")
    win.geometry("450x300")

    tk.Label(win, text="💼 Магазин Сидоровича", font=("Arial", 16)).pack(pady=10)
    for art in artifacts:
        btn = tk.Button(win, text=f"{art['name']} — {art['price']}₴\n{art['description']}", font=("Arial", 11),
                        command=lambda a=art: buy_artifact(a), wraplength=400, justify='left')
        btn.pack(fill='x', padx=10, pady=5)

def buy_artifact(artifact):
    global money
    if money >= artifact["price"]:
        inventory_artifacts.append(artifact)
        money -= artifact["price"]
        update_stats()
        messagebox.showinfo("Успіх", f"Ви придбали: {artifact['name']}")
    else:
        messagebox.showerror("Помилка", "Недостатньо грошей!")

# Головне вікно
#gitcoomit
root = tk.Tk()
root.title("Зона Відчуження")
root.geometry("600x400")
root.config(bg="#2b2b2b")

tk.Label(root, text="🎮 Вітаємо в грі Зона Відчуження", font=("Arial", 18), bg="#2b2b2b", fg="white").pack(pady=20)
stats = tk.Label(root, text="", font=("Arial", 13), bg="#2b2b2b", fg="lightgray")
stats.pack(pady=10)
update_stats()

btn_config = {"font": ("Arial", 14), "bg": "#444", "fg": "white", "padx": 10, "pady": 10}
tk.Button(root, text="📦 Інвентар", command=inventory_window, **btn_config).pack(fill='x', padx=40, pady=5)
tk.Button(root, text="☢ Артефакти", command=show_artifacts, **btn_config).pack(fill='x', padx=40, pady=5)
tk.Button(root, text="🧔 До Сидоровича", command=shop, **btn_config).pack(fill='x', padx=40, pady=5)
tk.Button(root, text="❌ Вийти", command=root.quit, font=("Arial", 14), bg="#a00", fg="white").pack(fill='x', padx=40, pady=10)

root.mainloop()
