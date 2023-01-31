# turtle_dead.py
import turtle

#configure turtle objects
wn = turtle.Screen()
wn.bgcolor("light green")
conrad = turtle.Turtle()
conrad.shape("turtle")
conrad.color("blue")
conrad.pensize(4)
#drawing clock

for i in range(100):
    conrad.penup()
    conrad.forward(100)
    conrad.pendown()
    conrad.forward(10)
    conrad.penup()
    conrad.forward(20)
    conrad.stamp()
    conrad.backward(130)
    conrad.right(360 / 12)

wn.exitonclick()