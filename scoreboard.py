from turtle import Turtle

# CONSTANTS
POSITION_Y = 300
FONT = ("Courier", 28, "bold")


# The Scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        super().color("white")
        super().ht()
        super().penup()
        super().goto(0, POSITION_Y)
        self.score = 0
        self.update_score()

    # Method for updating score
    def update_score(self):
        super().clear()
        super().write(f"Score: {self.score}", move=False, align="center", font=FONT)
