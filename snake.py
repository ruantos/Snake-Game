from turtle import Turtle

passo = 20

class Snake:
    def __init__(self, size):
        self.corpo = []
        self.criar(size)
        self.head = self.corpo[0]

    def criar(self, size, color="black"):
        for i in range(size):
            segmento = Turtle(shape="square")
            segmento.color(color)
            segmento.penup()
            segmento.goto(-20*i, 0)
            self.corpo.append(segmento)

    def mover(self):
        for segmento in range(len(self.corpo) -1, 0 , -1):
            x = self.corpo[segmento -1].xcor()
            y = self.corpo[segmento -1].ycor()
            self.corpo[segmento].goto(x, y)
        self.corpo[0].fd(passo)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)    
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def down(self):
        if self.head.heading() != 90:
           self.head.setheading(270)
