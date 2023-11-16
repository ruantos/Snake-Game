from turtle import Screen

def Tela(title="Jogo da cobrinha",
        width=700,
        heigth=700,
        background="blue"):
        screen = Screen()
        screen.title(title)
        screen.setup(width=width, height=heigth)
        screen.bgcolor(background)
        screen.exitonclick()
        return screen