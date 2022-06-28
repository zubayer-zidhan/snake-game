from turtle import Turtle

# CONSTANTS
POSITION_Y = 320


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
        self.game_on = False
