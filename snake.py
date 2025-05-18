from tkinter import *
from random import *

#крчстанти
WIDTH = 400
HEIGHT = 400
score = 0
SPASE_SIZE = 20
FOOD_COLOR = "red"

class Snake:
    pass
class Food:
    def __init__(self):
        x = randint(0, (WIDTH - SPASE_SIZE) - 1)*SPASE_SIZE
        y = randint(0, (HEIGHT - SPASE_SIZE) - 1)*SPASE_SIZE
        self.coords = (x, y)
        self.food = canvas.create_rectangle(x, y, x + SPASE_SIZE, y + SPASE_SIZE, fill="red")

root = Tk()
root.title("Snake Game")
root.resizable(False, False)
root.config(bg="black")


lbl_score = Label(root, text="Score: {}".format(score),bg="black", fg="white")
lbl_score.pack()

canvas = Canvas(root, width=400, height=400, bg="black")
canvas.pack()

root.geometry("400x400")

food = Food()

root.mainloop()