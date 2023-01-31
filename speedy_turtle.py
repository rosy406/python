import turtle
import random

window = turtle.Screen()

racer_1 = turtle.Turtle()
racer_1.up()
racer_1.shape("turtle")
racer_1.color(random.random(), random.random(), random.random())
racer_1.goto(-200, 100)
racer_1.down()
racer_1.stamp()

racer_2 = turtle.Turtle()
racer_2.up()
racer_2.shape("turtle")
racer_2.color(random.random(), random.random(), random.random())
racer_2.goto(-200, 75)
racer_2.down()
racer_2.stamp()

racer_3 = turtle.Turtle()
racer_3.up()
racer_3.shape("turtle")
racer_3.color(random.random(), random.random(), random.random())
racer_3.goto(-200, 50)
racer_3.down()
racer_3.stamp()

def is_winner(turtle):
    return turtle.xcor() >= 20

def reset():
    racer_1.penup()
    racer_2.penup()
    racer_3.penup()
    racer_1.goto(-200, 100)
    racer_2.goto(-200, 75)
    racer_3.goto(-200, 50)
    racer_1.pendown()
    racer_2.pendown()
    racer_3.pendown()

conrad = turtle.Turtle()
conrad.penup()
conrad.goto(20,200)
conrad.pendown()
conrad.right(90)
conrad.forward(200)
t1 = 0
t2 = 0
t3 = 0
moves = 0
for i in range(100):
    while moves <= 10:
        racer_1.forward(random.randint(1, 40))
        racer_1.dot()
        if is_winner(racer_1):
            print("racer_1 wins!")
            reset()
            t1 += 1
            break
        racer_2.forward(random.randint(1, 40))
        racer_2.dot()
        if is_winner(racer_2):
            print("racer_2 wins!")
            reset
            t2 += 1
            break
        racer_3.forward(random.randint(1, 40))
        racer_3.dot()
        if is_winner(racer_3):
            print("racer_3 wins!")
            reset()
            t3 +=1
            break
        moves += 1
    


 

    



    

# if racer_1.xcor() > racer_2.xcor():
#     print("Turtle racer #1 wins!")
# else:
#     print("Turtle racer #2 wins!")
                      
                      
window.exitonclick()
    