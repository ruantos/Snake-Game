from turtle import Screen, Turtle
import time

class Score(Turtle):
    def __init__(self, over=False):
        super().__init__()
        self.color("white")
        self.pontos = 0
        with open("highscore.txt", mode="r") as file:
            self.max_pontos = int(file.read())
        self.hideturtle()
        self.penup()
        if over:
            self.goto(0, 0) 
        else:
            self.goto(0, 300)
            self.refresh()


    def refresh(self):
        self.write(arg=f"Pontuação: {self.pontos}    Max: {self.max_pontos}",
                move=False,
                align="Center",
                font=("Arial", 14, "bold"))
        
    def add(self):
        self.pontos += 1
        self.undo()
        self.refresh()

    def reset(self):
        if self.pontos > self.max_pontos:
            self.max_pontos = self.pontos
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.max_pontos))
        self.undo()
        self.pontos = 0
        self.refresh()

    def over(self):
        self.write(arg=f"GAME OVER",
                move=False,
                align="Center",
                font=("Arial", 20, "bold"))
        

def Tela(title="Jogo da cobrinha",
    width=700,
    heigth=700,
    background="black"):
    screen = Screen()
    screen.title(title)
    screen.setup(width=width, height=heigth)
    screen.bgcolor(background)
    screen.tracer(0)
    return screen