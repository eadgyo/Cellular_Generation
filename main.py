from tkinter import *
from Model import Model
from Operation import Operation
import time
from random import random
from Vector3D import Vector3D

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

    canvas.create_line(60,60, 90, 60)
    operations = []
    operations.append(Operation("Ir", [1, 2], 1, 0.7, 0.2))
    operations.append(Operation("Il", [0, 2], 0, 0.7, 0.0, 0, 1))
    operations.append(Operation("Q1", [3, 4], 0, 0.6, 0.2))
    operations.append(Operation("Q2", [3, 2], 1, 0.5, 0.2))
    operations.append(Operation("Q3", [3, 2], 0, 0.5, 0.2))
    operations.append(Operation("T", [], 1, 0.5, 0.2, 0))

    points = []
    a = 600
    ra = 60
    points.append(Vector3D(0 + ra*(random() - 0.5),0 + ra*(random() - 0.5)))
    points.append(Vector3D(a + ra*(random() - 0.5),0 + ra*(random() - 0.5)))
    points.append(Vector3D(a + ra*(random() - 0.5),a + ra*(random() - 0.5)))
    points.append(Vector3D(0 + ra*(random() - 0.5),a + ra*(random() - 0.5)))

    celMod = Model(points, operations)
    celMod.draw(canvas)

    canvas.pack()
    fenetre.mainloop()
