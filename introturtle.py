# lesson 3-1.py

import turtle

wn = turtle.Screen()        # creates a screen/window
wn.bgcolor("black")

conrad = turtle.Turtle()    # creates a turtle object
conrad.shape("turtle")
conrad.color("orange", "black")
conrad.pensize(1)

conrad.begin_fill()
for i in range(100):
    conrad.forward(100)
    conrad.right(91)
conrad.end_fill()
# conrad.forward(100)
# conrad.right(120)
# conrad.forward(100)
# conrad.right(120)
# bob = turtle.Turtle()
# bob.shape("turtle")
# bob.forward(100)

# conrad.speed(1)
# conrad.forward(10)
# conrad.right(90)
# conrad.forward(100)
# conrad.right(90)
# conrad.forward(10)
# conrad.right(90)
# conrad.forward(100)
# conrad.penup()
# conrad.goto(-100, 100)
# conrad.pendown()
# conrad.forward(100)
# bob.right(90)
# bob.hideturtle()             #bob goes incognit0
# bob.forward(200)
# bob.showturtle()
















wn.exitonclick()
