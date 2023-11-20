from turtle import Turtle
from random import randint

class Fruta(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("black")
        self.speed("fastest")
        self.move()

    def move(self):
        self.goto(x=randint(-300, 300),
                y=randint(-300, 300))
