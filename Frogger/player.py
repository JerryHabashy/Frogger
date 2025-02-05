from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.resetPos()

    def up(self):
        self.forward(MOVE_DISTANCE)

    def resetPos(self):
        self.goto(STARTING_POSITION)