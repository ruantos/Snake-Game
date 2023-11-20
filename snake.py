from turtle import Turtle

passo = 20

class Cobra:
    def __init__(self, size, color="white"):
        self.corpo = []
        self.size = size
        self.color = color
        self.criar()
        self.head = self.corpo[0]

    def add(self):
        segmento = Turtle(shape="square")
        segmento.color(self.color)
        segmento.penup()
        if len(self.corpo) > 2:
            segmento.goto(self.corpo[-1].position())
        self.corpo.append(segmento)
        return segmento

    def criar(self):
        for i in range(self.size):
            segmento = self.add()
            segmento.goto(-20*i, 0)

    def move(self):
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

    def colisao(self):
        if self.head.xcor() > 320 or self.head.xcor() < -320 or self.head.ycor() > 320 or self.head.ycor() < -320:
            return True
    
    def bdcolisao(self):
        for segmento in self.corpo[1:]:
            if self.head.distance(segmento) < 10:
                return True