from turtle import Screen, Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pontos = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.write(arg=f"Pontuação: {self.pontos}",
                move=False,
                align="Center",
                font=("Arial", 14, "bold"))
    def add(self):
        self.pontos += 1
        self.undo()
        self.write(arg=f"Pontuação: {self.pontos}",
                move=False,
                align="Center",
                font=("Arial", 14, "bold"))
        
    def over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER",
                move=False,
                align="Center",
                font=("Arial", 18, "bold"))

        
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