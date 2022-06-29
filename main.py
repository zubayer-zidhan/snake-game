from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameOver import GameOver
import time

# CONSTANTS
SNAKE_SPEED = 0.09

# TODO: Set up Screen
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")

screen.tracer(0)


# --------- Create objects of the different classes ---------
snake = Snake()
food = Food()
scoreboard = Scoreboard()
gameOver = GameOver()


# ----------------- Implement snake movement -----------------
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
screen.onkey(key="Escape", fun=gameOver.game_over)


# ----------------- Game logic -----------------
screen.listen()


while gameOver.game_on:
    time.sleep(SNAKE_SPEED)
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 13:
        scoreboard.score += 1
        scoreboard.update_score()

        # Extend the snake
        snake.extend()

        # Create new food on the screen
        food.create_food()

    # Detect collision with wall
    if snake.head.xcor() < -340 or snake.head.xcor() > 340 or snake.head.ycor() < -340 or snake.head.ycor() > 340:
        gameOver.game_over()

    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 9:
            gameOver.game_over()


# Mainloop
screen.mainloop()
