from turtle import Turtle
from random import randint

# CONSTANTS
P_INT = 310     # positive integer upper bound
I_INT = -310    # negative integer upper bound

# The Food class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        super().shape("circle")
        super().color("white")
        super().shapesize(stretch_wid=0.9, stretch_len=0.9)
        super().penup()
        self.create_food()

    def create_food(self):
        random_x = randint(I_INT, P_INT)
        random_y = randint(I_INT, P_INT)
        super().goto(random_x, random_y)
