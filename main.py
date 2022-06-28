from turtle import Screen
from snake import Snake
from food import Food
import time

# CONSTANTS
SNAKE_SPEED = 0.09

# TODO: Set up Screen
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")

screen.tracer(0)


# TODO: Create objects of the different classes
snake = Snake()
food = Food()


# Game on
game_on = True


# Temp functions to be changed later
def game_over():
    global game_on
    game_on = False


# TODO: Implement snake movement
# wasd key functionality
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)

# arrow key functionality
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)

# Escape key functionality
screen.onkey(key="Escape", fun=game_over)


# TODO: Game logic
screen.listen()



while game_on:
    time.sleep(SNAKE_SPEED)
    screen.update()
    snake.move()




# TODO: Generate food


# TODO: Detect collision with wall








# End of file
screen.exitonclick()
