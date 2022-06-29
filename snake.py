from turtle import Turtle

# CONSTANTS
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


# The Snake class
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Create a snake segment
    def create_snake_segment(self, coordinates):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.goto(coordinates)
        self.segments.append(new_segment)

    # Extend the snake
    def extend(self):
        coor = self.segments[-1].pos()
        self.create_snake_segment(coor)

    # Create the initial snake
    def create_snake(self):
        for coordinates in STARTING_POSITIONS:
            self.create_snake_segment(coordinates)

    # Move the snake
    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    # On pressing w
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # On pressing a
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # On pressing s
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # On pressing d
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
