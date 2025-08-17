from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.python = []
        self.create_snake()
        self.head = self.python[0]

    def create_snake(self):
        for position in STARTING_POSITION:
           self.add_block(position)

    def add_block(self,position):
        body = Turtle(shape='square')
        body.color('red')
        body.penup()
        body.goto(position)
        self.python.append(body)

    def reset(self):
        for pamu in self.python:
            pamu.goto(1000,1000)
        self.python.clear()
        self.create_snake()
        self.head = self.python[0]

    def extend(self):
        self.add_block(self.python[-1].position())

    def move(self):
        for pamu in range(len(self.python)-1,0,-1):
            new_x = self.python[pamu-1].xcor()
            new_y = self.python[pamu-1].ycor()
            self.python[pamu].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)