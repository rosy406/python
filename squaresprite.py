import turtle
wn = turtle.Screen()
conrad = turtle.Turtle()
conrad.shape("turtle")
wn.bgcolor("black")
conrad.pencolor("white")
conrad.pensize(5)
conrad.speed(10)
conrad.penup()
conrad.goto(100,100)
conrad.setheading(270)
conrad.pendown()
for i in range(4):
    conrad.forward(200)
    for i in range(8):
        conrad.forward(30)
        conrad.back(30)
        conrad.right(45)
    conrad.right(90)
wn.exitonclick()
