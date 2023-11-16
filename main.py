""" Snake Game """

from turtle import Turtle, Screen
from screen import Tela
from body import Criar
from move import Mover
tela = Tela()
cobra = Criar()
tela.update()


on = True
while on:
    tecla = tela.listen()
    Mover(cobra, tela, tecla)


tela.exitonclick()





