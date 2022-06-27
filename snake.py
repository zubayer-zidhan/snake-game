from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    # Create a snake segment
    def create_snake_segment(self, coordinates):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.goto(coordinates)
        self.snake_segments.append(new_segment)

    # Create the initial snake
    def create_snake(self):
        for coordinates in STARTING_POSITIONS:
            self.create_snake_segment(coordinates)

    # Move the snake
    def move(self):
        for segment in self.snake_segments:
            segment.fd(10)

    # On pressing a
    def turn_left(self):
        heading = self.snake_head.heading()
        self.snake_head.setheading(heading - 90)

    # On pressing d
    def turn_right(self):
        heading = self.snake_head.heading()
        self.snake_head.setheading(heading + 90)


