import turtle as t 
import random

wn = t.Screen()
conrad = t.Turtle()
conrad.shape("turtle")
wn.bgcolor("black")
counter = 1

def is_screen(window,turtle):
    max_x = window.window_width() // 2
    max_y = window.window_height() // 2
    x = turtle.xcor() 
    y = turtle.ycor()
    if x >= max_x or x <= -max_x:
      return False
    elif y >= max_y or y <= -max_y:
        return False
    else:
        return True
    

while is_screen(wn,conrad):
    number = random.randint(1,2)
    if number == 1:
        conrad.right(120)
    else:
        conrad.left(120)
    
    if counter % 5 == 0:
        conrad.color(random.random(), random.random(), random.random())
    conrad.pensize(random.randint(1,9))
    conrad.speed(random.randint(1,10))
    conrad.forward(20)
    counter = counter + 1
    






wn.exitonclick()
