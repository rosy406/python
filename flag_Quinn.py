# -----------------------------------------+
# Quinn Rosenstock                               |
# Computer Science, Project 4              |
# Last Updated: October 19, 2022                   |
# -----------------------------------------|
# Define and comment the two missing       |
# functions such that the desired          |
# Conservation Partnership flag is drawn.  |
# -----------------------------------------+

import turtle

# Your functions go here 


window = turtle.Screen()
flag = turtle.Turtle()
flag.hideturtle()
flag.speed(0)


#defining the draw star funtion
def draw_star(turtle, color, length, leftxcor, leftycor):
     #setting colors for stars
     turtle.color(color)
     turtle.begin_fill()
     turtle.pendown()
     #for loop that draws each star
     for i in range(5):
        turtle.forward(20)
        turtle.right(144)
     turtle.end_fill()
    
    
#defining draw_rectangle
def draw_rectangle(turtle,color,length,width,x,y):
    turtle.penup()
    turtle.goto(x,y)
    #setting color of flag
    flag.color(color)
    turtle.pendown()
    #for loop to draw each rectangle
    for i in range(2):
        turtle.begin_fill()
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
        turtle.end_fill()

# initially, make the background of the entire flag black
# the dimensions of the flag are 450 by 330
# the upper left corner of the flag is at (-225, 165)
draw_rectangle(flag, "black", 450, 330, -225, 165)

# draw the yellow and red stripes
y = 110
for i in range(2):
    draw_rectangle(flag, "yellow", 450, 55, -225, y)
    draw_rectangle(flag, "red", 450, 55, -225, y - 55)
    y = y - 165

# draw the black square in the center
draw_rectangle(flag, "green", 180, 180, -90, 90)

# draw the 13 white stars
flag.penup()
flag.goto(-70, 10)
for i in range(13):
    # each of the 5 lines of the star is 20 pixels
    # the left side of the horizontal line is at (flag.xcor(), flag.ycor())
    draw_star(flag, "white", 20, flag.xcor(), flag.ycor())
    flag.penup()
    flag.forward(140)
    flag.right(180 - 180/13)

window.exitonclick()