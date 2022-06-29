from turtle import Turtle

# CONSTANTS
FONT = ("Courier", 28, "bold")


# The Scoreboard class
class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        super().color("white")
        super().ht()
        super().penup()
        super().home()
        self.game_on = True

    # Method for updating score
    def game_over(self):
        super().write("Game Over.", move=False, align="center", font=FONT)
        self.game_on = False
