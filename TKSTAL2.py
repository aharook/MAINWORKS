import tkinter as tk
from tkinter import messagebox
import random

money = 1000
HP = 100
radiation = 0
hungruy = 0
armor = 0
ammo = {
    "Пістолет": 10,
    "Автомат": 0,
    "Снайперська гвинтівка": 0
}
bg = "#2b2b2b"

artifacts = [
    {"name": "КРОВ КАМЕНЮ", "description": "Поступово відновлює здоров'я.", "effects": {"HP": 10}, "price": 150},
    {"name": "ДУША", "description": "Зменшує радіацію.", "effects": {"radiation": -5}, "price": 250},
    {"name": "СЕРЦЕ", "description": "Відновлює броню.", "effects": {"armor": 15}, "price": 220},
    {"name": "ПЛАСТИНА", "description": "Зменшує голод.", "effects": {"hungruy": -10}, "price": 100},
    {"name": "ЗАЩИТА", "description": "Зменшує радіацію.", "effects": {"radiation": -10}, "price": 200},
    {"name": "ПРИП'ЯТЬ", "description": "Відновлює броню.", "effects": {"armor": 20}, "price": 300},
    {"name": "СВІТЛО", "description": "Збільшує видимість у темряві.", "effects": {}, "price": 50},
    {"name": "ЧОРНА ДІРА", "description": "Зменшує голод.", "effects": {"hungruy": -5}, "price": 80},
]
inventory_artifacts = []

def update_stats():
    stats.config(text=f"❤️{HP}  ☢ {radiation}%   🍖 {hungruy}%   🛡 {armor}%   💰 {money}₴   🔫 Патрони: {sum(ammo.values())}")

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
    win.geometry("500x400")
    win.config(bg=bg)
    if not inventory_artifacts:
        tk.Label(win, text="⚠️ У вас немає артефактів", font=("Arial", 12), bg=bg, fg="white").pack(pady=20)
        return
    for i, art in enumerate(inventory_artifacts):
        btn = tk.Button(win, text=f"{i+1}. {art['name']} — {art['description']}", font=("Arial", 11), bg=bg, fg="#02d42f",
                        command=lambda i=i: use_artifact(i))
        btn.pack(fill='x', padx=10, pady=5)

def inventory_window():
    win = tk.Toplevel(root)
    win.title("Інвентар")
    win.geometry("400x300")
    win.config(bg=bg)
    tk.Label(win, text="📦 Ваш інвентар", font=("Arial", 16), bg=bg, fg="white").pack(pady=10)

    for weapon, count in ammo.items():
        tk.Label(win, text=f"{weapon} — {count} патронів", font=("Arial", 12), bg=bg, fg="white").pack(pady=2)

    def heal():
        global HP
        HP = min(100, HP + 20)
        update_stats()
        messagebox.showinfo("Аптечка", "Ви використали аптечку.")

    tk.Button(win, text="🩹 Використати аптечку", command=heal, font=("Arial", 12), bg="#28a745", fg="white").pack(pady=10)

def sidor():
    win = tk.Toplevel(root)
    win.title("Сидорович")
    win.geometry("450x400")
    win.config(bg=bg)
    
    tk.Label(win, text="гроші: " + str(money) + "₴", font=("Arial", 14), bg=bg, fg="white").pack(pady=10)
    tk.Label(win, text="💼 Магазин Сидоровича", font=("Arial", 16), bg=bg, fg="white").pack(pady=5)

    def show_artifact_buttons():
        for art in artifacts:
            btn = tk.Button(win, text=f"{art['name']} — {art['price']}₴\n{art['description']}",
                            font=("Arial", 11),
                            command=lambda a=art: buy_artifact(a),
                            wraplength=400, justify='left',
                            bg="#444", fg="white")
            btn.pack(fill='x', padx=10, pady=5)

    def buy_ammo(type_, price, quantity):
        global money
        if money >= price:
            money -= price
            ammo[type_] += quantity
            update_stats()
            messagebox.showinfo("Куплено", f"Ви купили {quantity} патронів для {type_}")
        else:
            messagebox.showerror("Помилка", "Недостатньо грошей!")

    tk.Button(win, text="🔫 Купити пістолетні патрони (10шт - 100₴)", command=lambda: buy_ammo("Пістолет", 100, 10), bg="#555", fg="white").pack(pady=2)
    tk.Button(win, text="🔫 Купити автоматні патрони (20шт - 250₴)", command=lambda: buy_ammo("Автомат", 250, 20), bg="#555", fg="white").pack(pady=2)
    tk.Button(win, text="🔫 Купити снайперські патрони (5шт - 200₴)", command=lambda: buy_ammo("Снайперська гвинтівка", 200, 5), bg="#555", fg="white").pack(pady=2)

    tk.Button(win, text="🛒 Придбати артефакти", command=show_artifact_buttons, font=("Arial", 12), bg="#28a745", fg="white").pack(pady=10)
    tk.Button(win, text="❌ Вийти", command=win.destroy, font=("Arial", 12), bg="#a00", fg="white").pack(pady=10)

def buy_artifact(artifact):
    global money
    if money >= artifact["price"]:
        inventory_artifacts.append(artifact)
        money -= artifact["price"]
        update_stats()
        messagebox.showinfo("Успіх", f"Ви придбали: {artifact['name']}")
    else:
        messagebox.showerror("Помилка", "Недостатньо грошей!")

def start_shooting_range():
    range_win = tk.Toplevel(root)
    range_win.title("🎯 Тир")
    range_win.geometry("500x500")
    range_win.config(bg=bg)

    score = tk.IntVar(value=0)
    time_left = tk.IntVar(value=30)

    tk.Label(range_win, text="🎯 Попади в 20 цілей за 30 секунд", font=("Arial", 14), bg=bg, fg="white").pack(pady=10)
    score_label = tk.Label(range_win, textvariable=score, font=("Arial", 12), bg=bg, fg="white")
    score_label.pack()

    canvas = tk.Canvas(range_win, width=400, height=300, bg="#1e1e1e", highlightthickness=0)
    canvas.pack(pady=10)

    def create_target():
        canvas.delete("all")
        x, y = random.randint(10, 360), random.randint(10, 260)
        target = canvas.create_text(x, y, text="🍾", font=("Arial", 24), fill="red", tags="target")

        target_hit = {"value": False}

        def on_click(event):
            if not target_hit["value"]:
                canvas.delete(target)
                target_hit["value"] = True
                score.set(score.get() + 1)
                update_stats()
                if score.get() >= 20:
                    messagebox.showinfo("Перемога", "🎉 Ви виграли! Тренування завершено.")
                    range_win.destroy()
                else:
                    range_win.after(300, create_target)

        canvas.tag_bind("target", "<Button-1>", on_click)

        def remove_if_not_hit():
            if not target_hit["value"]:
                canvas.delete("target")
                if time_left.get() > 0:
                    range_win.after(300, create_target)

        canvas.after(2000, remove_if_not_hit)

    def update_timer():
        if time_left.get() > 0:
            time_left.set(time_left.get() - 1)
            timer_label.config(text=f"⏱ Час: {time_left.get()} сек")
            range_win.after(1000, update_timer)
        elif score.get() < 20:
            messagebox.showinfo("Поразка", f"❌ Ви не встигли. Влучено: {score.get()}")
            range_win.destroy()

    timer_label = tk.Label(range_win, text="", font=("Arial", 12), bg=bg, fg="white")
    timer_label.pack()

    tk.Button(range_win, text="🚪 Покинути тир", command=range_win.destroy, font=("Arial", 12), bg="#a00", fg="white").pack(pady=10)

    create_target()
    update_timer()


root = tk.Tk()
root.title("Зона Відчуження")
root.geometry("600x450")
root.config(bg=bg)

tk.Label(root, text="🎮 Вітаємо в Ceлі Новачків", font=("Arial", 18), bg=bg, fg="white").pack(pady=20)
stats = tk.Label(root, text="", font=("Arial", 13), bg=bg, fg="lightgray")
stats.pack(pady=10)
update_stats()

btn_config = {"font": ("Arial", 14), "bg": "#444", "fg": "white", "padx": 10, "pady": 10}
tk.Button(root, text="📦 Інвентар", command=inventory_window, **btn_config).pack(fill='x', padx=40, pady=5)
tk.Button(root, text="☢ Артефакти", command=show_artifacts, **btn_config).pack(fill='x', padx=40, pady=5)
tk.Button(root, text="🧔 До Сидоровича", command=sidor, **btn_config).pack(fill='x', padx=40, pady=5)
tk.Button(root, text="🎯 Піти в тир", command=start_shooting_range, **btn_config).pack(fill='x', padx=40, pady=5)
tk.Button(root, text="❌ Вийти", command=root.quit, font=("Arial", 14), bg="#a00", fg="white").pack(fill='x', padx=40, pady=10)

root.mainloop()

