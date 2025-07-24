from turtle import Turtle

FINISH_LINE_Y = 280
STARTING_POSITION = (0, -280)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(10)

    def is_at_finish(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)
