import turtle




wn = turtle.Screen()
bob = turtle.Turtle()
def draw_star():
    for i in range(5):
        bob.forward(100)
        bob.right(144)

draw_star()
wn.exitonclick()