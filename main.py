from tkinter import *
from Model import Model
from Operation import Operation
import time
from random import random

def clavier(event):
    global coords

    touche = event.keysym
    """
    if touche == "Up":
        print("Up")
        coords = (coords[0], coords[1] - 10)
    elif touche == "Down":
        coords = (coords[0], coords[1] + 10)
    elif touche == "Right":
        coords = (coords[0] + 10, coords[1])
    elif touche == "Left":
        coords = (coords[0] -10, coords[1])
    """
    canvas.delete(ALL)
    celMod.update()
    celMod.draw(canvas)


if __name__ == "__main__":
    fenetre = Tk()
    canvas = Canvas(fenetre, width=800, height=800, background='white')

    canvas.focus_set()
    canvas.bind("<Key>", clavier)

    for i in range(5000):
        a = random()
        assert(0 <= a <= 1.0)
    operations = []
    operations.append(Operation("Ir", [1, 2], 1, 0.7, 0.2))
    operations.append(Operation("Il", [0, 2], 0, 0.7, 0.0, 0, 1))
    operations.append(Operation("Q1", [3, 4], 0, 0.6, 0.2))
    operations.append(Operation("Q2", [2, 2], 1, 0.5, 0.2))
    operations.append(Operation("Q3", [5, 5], 0, 0.5, 0.2))
    operations.append(Operation("T", [], 1, 0.5, 0.2, 0))

    celMod = Model(0, 0, 200, 200, operations)
    celMod.draw(canvas)

    canvas.pack()
    fenetre.mainloop()
