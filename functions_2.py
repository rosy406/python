#function that outputs area of a circle
def circle_area(radius):
    area = (radius ** 2 * 3.1415)
    return area


    


#print(circle_area(2))

def rectangle_area(length, width):
    area = length * width
    return area


#print("the area of the rectangle is",rectangle_area(2,4))
#def fancy_square():
import turtle
wn = turtle.Screen()
conrad = turtle.Turtle()

def draw_tri(turtle, length):
    for i in range(3):
        turtle.forward(length)
        turtle.right(120)






def draw_sprite(turtle, legs, length):
    for i in range(legs):
        turtle.forward(length)
        draw_tri(conrad, 30)
        turtle.backward(length)
        turtle.right(360/legs)

def draw_square(turtle, length):
    for i in range (4):
        turtle.forward(length)
        draw_sprite(conrad, 8,20 )
        turtle.right(90)
        


draw_square(conrad,150)










wn.exitonclick()