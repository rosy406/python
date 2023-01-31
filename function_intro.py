#function_intro.py
from tkinter import Y
import turtle as t

wn =t.Screen()
wn.bgcolor("white")
conrad = t.Turtle()
conrad.color("black")
conrad.pensize(5)
conrad.speed(10)

def draw_square(turtle, length):
    for i in range(4):
        conrad.left(90)
        conrad.forward(length)




length = 20
y = -10
x = 10
for i in range(100):
    draw_square(conrad, length)
    conrad.penup()
    conrad.goto(x, y)
    conrad.pendown()
    length = length + 20
    y = y - 10
    x = x + 10








wn.exitonclick()