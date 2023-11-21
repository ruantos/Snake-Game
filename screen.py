from turtle import Screen, Turtle
import time

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pontos = 0
        self.max_pontos = 0
        self.hideturtle()
        self.penup()
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
        self.undo()
        self.pontos = 0
        self.refresh()

        
class Over(Turtle):
    def __init__(self):
        self.goto(0, 0)
        self.penup()
        self.hideturtle()

    def over(self, pontos):
        self.write(arg=f"GAME OVER\n\nSUA PONTUAÇÃO: {pontos}",
                move=False,
                align="Center",
                font=("Arial", 20, "bold"))
        time.sleep(3)
        self.undo()

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