from snake import Cobra
from screen import Tela, Score
from fruit import Fruta
import time

cobra = Cobra(3)
tela = Tela()
fruta = Fruta()
placar = Score()
over = Score(True)

tela.update()
tela.listen()

over.goto(0, 10)
while over.count > 0:
    over.start()
    tela.update()
    time.sleep(1)
    over.undo()
over.goto(0, 0)

on = True
while on:
    tela.update()
    time.sleep(0.06)
    cobra.move()
    tela.onkey(cobra.up, "Up")
    tela.onkey(cobra.down, "Down")
    tela.onkey(cobra.left, "Left")
    tela.onkey(cobra.right, "Right")
    if cobra.head.distance(fruta) < 15:
        fruta.move()
        cobra.add()
        placar.add()
    if cobra.colisao() or cobra.bdcolisao():
        over.over()
        tela.update()
        over.undo()
        time.sleep(3)

        placar.reset()
        cobra.reset()


tela.exitonclick()