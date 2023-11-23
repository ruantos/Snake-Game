from turtle import Screen, Turtle
import time

class Score(Turtle):
    def __init__(self, over=False):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pontos = 0
        self.max_pontos = self.get_highscore()
        self.count = 3
        if over:
            self.goto(0, 0) 
        else:
            self.goto(0, 300)
            self.refresh()


    def get_highscore(self):
        with open("highscore.txt", mode="r") as file:
            max_pontos = int(file.read())
        return max_pontos
     
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
        
    def start(self):
        self.write(arg=f"{self.count}",
                move=False,
                align="Center",
                font=("Arial", 20, "bold"))
        self.count -= 1

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