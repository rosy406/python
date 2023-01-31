length = input("how long do you want the sides to be?: ")
length = int(length)
sides = int(input("how many sides do you want?: "))
color = input("what color do you want the outside to be?: ")
fill = input("what do you want the inside to be?: ")
import turtle 

wn = turtle.Screen()
wn.bgcolor("black")

conrad = turtle.Turtle()
conrad.shape("turtle")
conrad.color(color, fill)
conrad.pensize(5)
conrad.speed(5)
conrad.begin_fill()

for side in range(sides):
    conrad.forward(length)
    conrad.right(360 / sides)

conrad.end_fill()

wn.exitonclick()
#ask for number of sides, length, fill color, outside color