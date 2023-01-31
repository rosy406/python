
#1
# import statistics

# numbers = [1, 2, 3, 4, 5, 4, 6]
# print(statistics.mode(numbers))

#2
# def boardwalk_rent(houses):
#     if houses == 0:
#         return 50
#     elif houses == 1:
#         return 200
#     elif houses == 2:
#         return 600
#     elif houses >= 3:
#         return "unknown"
    




# print(boardwalk_rent(0))
# print(boardwalk_rent(1))
# print(boardwalk_rent(2))
# print(boardwalk_rent(3))




#4
#decagon function
import turtle
import random


def decagon(turtle,length):
    for i in range (10):
        Tcolor = random.randint(1, 2)
        if Tcolor == 1:
            turtle.color("orange")
        else:
            turtle.color("black")
        turtle.forward(length)
        turtle.right(36)


wn = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.pensize(10)
decagon(my_turtle, 50)
wn.exitonclick()



