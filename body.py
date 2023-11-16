from turtle import Turtle

def Create(shape="square",size=3):
    snake = [Turtle(shape=shape) for _ in range(size)]
    for i in range(size):
        snake[i].goto(-20*i, 0)
    return snake