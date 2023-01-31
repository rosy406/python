#practice_practicum6.py
#1
# import turtle
# window = turtle.Screen()
# circle = turtle.Turtle()
# def draw_circle(turtle, x, y,radius, color):
#     turtle.penup()
#     turtle.goto(x,y)
#     turtle.pendown()
#     turtle.dot()
#     turtle.dot(radius,color)


# draw_circle(circle, 0, 0, 50, "red")
# draw_circle(circle,-100, 200, 75, "blue")



# window.exitonclick()

#2
# year = int(input("Enter the year you want to categorize: "))
# if year >= 1600:
#     print("Modern Period")
# elif year >= 1300 and year < 1600:
#     print("Late Medieval Period")
# elif year >= 1000 and year <1300:
#     print("High medieval Period")
# elif year >= 300 and year <1000:
#     print("Early Medeval Period")
# elif year >= 0 and year < 300:
#     print("Ancient Period")






#3
import turtle 
import random

runner = turtle.Turtle()

def move(x, y):
    for i in range(20):
        direction = random.randint(1, 2)

        if direction == 1:
            runner.left(120)
        else:
            runner.right(120)
    
        runner.forward(50)

turtle.onscreenclick(move)

input()
#the code creates a function move, that randomly chooses either 1 or 2 then gives that value to the variable 
#direction. it then creates an if else statement that turns the turtle either lef or right
#depending on the number assigned to it. It the moves it forward 50



