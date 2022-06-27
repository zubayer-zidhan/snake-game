from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Create a snake segment
    def create_snake_segment(self, coordinates):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.goto(coordinates)
        self.segments.append(new_segment)

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
        self.head.fd(10)

    # On pressing a
    def turn_left(self):
        heading = self.head.heading()
        self.head.setheading(heading - 90)

    # On pressing d
    def turn_right(self):
        heading = self.head.heading()
        self.head.setheading(heading + 90)


