from turtle import Turtle, Screen
import time

def Mover(cobra, tela, tecla):
    tela.update()
    time.sleep(0.1)
    if tecla:
        tela.onkey(Up, "Up")
        tela.onkey(Down, "Down")
        tela.onkey(Left, "Left")
        tela.onkey(Right, "Right")
    for segmento in cobra:
        segmento.forward(20)


cobra = Turtle
def Up(cobra):
    cobra.
