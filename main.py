from snake import Snake
from screen import Tela
import time

cobra = Snake(3)

tela = Tela()
tela.update()
tela.listen()

on = True
while on:
    tela.update()
    time.sleep(0.1)
    cobra.mover()
    tela.onkey(cobra.up, "w")
    tela.onkey(cobra.down, "s")
    tela.onkey(cobra.left, "a")
    tela.onkey(cobra.right, "d")


tela.exitonclick()