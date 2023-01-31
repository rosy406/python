# -----------------------------------------+
# Quinn Rosenstock                         |
# Computer Science, Project 5              |
# Last Updated: Nov 2, 2022                   |
# -----------------------------------------|
# Use the random module to create a        |
# simulated ecosystem by stamping randomly |
# colored animals in random locations with |
# random orientations.                     |
# -----------------------------------------+
# we worked together on every variable
from tkinter import Y
import turtle
import random

# -----------------------------------------+
# create_animal                            |
# -----------------------------------------+
# This function has no parameters.         |
# -----------------------------------------+
# Create and return a hidden turtle with   |
# speed 0 and pensize 10.                  |
# -----------------------------------------+

def create_animal():
    conrad = turtle.Turtle()
    #conrad.hideturtle()
    conrad.speed(0)
    conrad.pensize(10)
    return conrad

# -----------------------------------------+
# draw_boundary                            |
# -----------------------------------------+
# the_animal: the animal to draw with      |
# max_x: window's upper right x coordinate |
# max_y: window's upper right y coordinate |
# -----------------------------------------+
# Draw a rectangle around the window whose |
# lower left coordinate is (-max_x, -max_y)|
# and whose upper right coordinate is      |
# (max_x, max_y).                          |
# -----------------------------------------+

def draw_boundary(the_animal, max_x, max_y):
    the_animal.penup()
    the_animal.goto(max_x, max_y)
    the_animal.pendown()
    the_animal.goto(-max_x, max_y)
    the_animal.goto(-max_x,-max_y)
    the_animal.goto(max_x,-max_y)
    the_animal.goto(max_x,max_y)
    the_animal.penup()


# -----------------------------------------+
# stamp_animal                             |
# -----------------------------------------+
# the_animal: the animal to draw with      |
# max_x: window's upper right x coordinate |
# max_y: window's upper right y coordinate |
# -----------------------------------------+
# Stamp an "animal" at a random coordinate |
# in the shape of either a turtle or a     |
# a "bird" (the "classic" shape) with a    | 
# random color and a random heading.       |  
# -----------------------------------------+

def stamp_animal(the_animal, max_x, max_y):
    shape = random.choice(["classic","turtle"])
    the_animal.shape(shape)
    the_animal.color(random.random(), random.random(), random.random())
    heading = random.randint(1,360)
    the_animal.setheading(heading)
    x = random.randint(-max_x,max_x)
    y = random.randint(-max_y,max_y)
    the_animal.goto(x,y)
    the_animal.stamp()

# -----------------------------------------+
# write_message                            |
# -----------------------------------------+
# the_animal: the animal to draw with      |
# message: the words that are written      |
# message_color: the color of the message  |
#  x: The x coordinate                     |
#  y: The y coordinate                     |
# fontname: The font of the message        |
# fontsize: the size of the font           |
# fonttype: the type of the font           |
# -----------------------------------------+
# write a message at the bottom of the     |
# screen saying who programed the code     |  
# -----------------------------------------+

def write_message(the_animal, message, message_color, x, y, fontname, fontsize, fonttype):
    the_animal.goto(x, y)
    the_animal.color(message_color)
    the_animal.write(message, font=(fontname, fontsize, fonttype))

# -----------------------------------------+
# The following code controls the logic for|
# Assignment 5.  Do not make any changes   |
# to it except to modify the "Program by"  |
# message to show your name.               |
# -----------------------------------------+

window = turtle.Screen()
stamper = create_animal()
how_many = random.randint(10, 20)
upper_right_x = window.window_width() // 2
upper_right_y = window.window_height() // 2
draw_boundary(stamper, upper_right_x, upper_right_y)
for stamp in range(how_many):
    stamp_animal(stamper, upper_right_x, upper_right_y)
message = "Animals = " + str(how_many)
write_message(stamper, message, "black", -75, -200, "Ariel", 20, "bold")
message = "Program by Quinn and Addy"
write_message(stamper, message, "purple", -75, -225, "Ariel", 12, "normal")

window.exitonclick()