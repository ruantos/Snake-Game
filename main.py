from snake import Cobra
from screen import Tela, Score
from fruit import Fruta
import time

cobra = Cobra(3)
tela = Tela()
fruta = Fruta()
placar = Score()

tela.update()
tela.listen()

on = True
while on:
    tela.update()
    time.sleep(0.06)
    cobra.mover()
    tela.onkey(cobra.up, "w")
    tela.onkey(cobra.down, "s")
    tela.onkey(cobra.left, "a")
    tela.onkey(cobra.right, "d")
    if cobra.head.distance(fruta) < 15:
        fruta.move()
        placar.pontos += 1 

