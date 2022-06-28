from turtle import Turtle
from random import randint


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
        random_x = randint(-320, 320)
        random_y = randint(-320, 320)
        super().goto(random_x, random_y)
