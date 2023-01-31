import turtle
import random

window = turtle.Screen()

square = turtle.Turtle()
square.speed(0)
square.hideturtle()

square.up()
square.goto(-200, 200)
square.down()

for i in range(4):
    square.forward(50)
    square.right(90)

square.up()
square.goto(-205, 205)
square.write("Change Color")

#bg color
box = turtle.Turtle()
box.speed(0)
box.hideturtle()
box.up()
box.goto(-300, 200)
box.down()

for i in range(4):
    box.forward(50)
    box.right(90)

box.up()
box.goto(-305, 205)
box.write("Change bg color")


cube = turtle.Turtle()
cube.speed(0)
cube.hideturtle()
cube.up()
cube.goto(-100, 200)
cube.down()

for i in range(4):
    cube.forward(50)
    cube.right(90)

cube.up()
cube.goto(-100, 205)
cube.write("pick pen up")


square = turtle.Turtle()
square.speed(0)
square.hideturtle()
square.up()
square.goto(-100, 200)
square.down()

for i in range(4):
    square.forward(50)
    square.right(90)

cube.up()
cube.goto(-100, 205)
cube.write("pick pen up")




pencil = turtle.Turtle()
pencil.shape("circle")

def drawing_controls(x, y):
    if (-200 <= x <= -150) and (150 <= y <= 200):
        pencil.color(random.random(), random.random(), random.random())  
    elif (-300 <= x <= -250) and (150 <= y <= 200):
        window.bgcolor(random.random(), random.random(), random.random()) 
    elif (-100 <= x <= -50) and (150 <= y <= 200):
        pencil.penup()
    elif (0 <= x <= 50) and (150 <= y <= 200):
        pencil.pendown()
window.onclick(drawing_controls)
pencil.ondrag(pencil.goto)






input()