 # -----------------------------------------+
  # Quinn Rosenstock                         |
  # Computer Science, Project 3              |
  # Last Updated: October 4th, 2022          |  
  # -----------------------------------------|
  # In this assignment I draw a Flame-       |
  # Crested Tanager.                         |
  # -----------------------------------------+




import turtle
wn = turtle.Screen()
conrad =turtle.Turtle()

conrad.speed(0)
conrad.penup()
conrad.goto(200,200)
conrad.pendown()

# make window
conrad.fillcolor("dodgerblue1")
conrad.begin_fill()
for i in range(4):
    conrad.right(90)
    conrad.forward(400)
conrad.end_fill()
conrad.penup()
conrad.goto(-200,-80)
conrad.pendown()

#head shape
conrad.fillcolor("black")
conrad.begin_fill()
conrad.left(65)
conrad.forward(100)

conrad.right(5)
conrad.goto(-112.50,71.55)
conrad.right(65)
conrad.forward(150)

conrad.right(85)
conrad.forward(40)
conrad.right(60)
conrad.forward(40)
conrad.left(120)

conrad.forward(25)


conrad.goto(23.94,-14.02)
conrad.right(120)

for i in range(20):
    conrad.forward(4)
    conrad.left(2)
conrad.goto(-33.91,-82.97)

conrad.goto(-50,-200)
conrad.setheading(180)
conrad.forward(150)
conrad.right(90)
conrad.forward(120)
conrad.end_fill()

#draw his crest
conrad.fillcolor("red")
conrad.begin_fill()
conrad.penup()
conrad.goto(-112.50,71.55)
conrad.pendown()
conrad.left(35)
conrad.forward(40)
conrad.right(125)
for i in range(30):
    conrad.forward(6)
    conrad.right(1)
conrad.goto(36.93,58.48)
conrad.goto(-112.50,71.55)
conrad.end_fill()

#draw his eye
conrad.fillcolor("grey10")
conrad.begin_fill()
conrad.goto(-20,50)
conrad.left(30)
for i in range(90):
    conrad.forward(1)
    conrad.right(4)
conrad.end_fill()
conrad.goto(-20,50)
conrad.setheading(270)
conrad.penup()
conrad.forward(7)
conrad.setheading(0)
conrad.pencolor("black")
conrad.fillcolor("black")
conrad.begin_fill()
conrad.pendown()
for i in range (45):
    conrad.forward(1)
    conrad.right(8)
conrad.end_fill()
conrad.penup()
#draw the beak
conrad.goto(36.93,58.48)
conrad.pendown()
conrad.fillcolor("grey20")
conrad.begin_fill()
conrad.setheading(270)
conrad.forward(25)
conrad.left(75)
conrad.forward(20)

for i in range(15):
    conrad.forward(4)
    conrad.right(3)
conrad.goto(23.94,-14.02)
conrad.right(150)
conrad.forward(25)
conrad.right(120)
conrad.forward(40)
conrad.left(60)
conrad.goto(36.93,33.48)

conrad.end_fill()

#make sun
conrad.fillcolor("yellow")
conrad.pencolor("yellow")
conrad.begin_fill()
conrad.penup()
conrad.goto(200,200)
conrad.pendown()
conrad.setheading(180)
conrad.forward(115)
conrad.left(90)
for i in range(90):
    conrad.forward(2)
    conrad.left(1)
conrad.forward(1)
conrad.goto(200,200)
conrad.end_fill()

#draw sprite of the sun
conrad.penup()
conrad.goto(200,200)
conrad.setheading(270)
conrad.pendown()
conrad.pencolor("yellow")
for i in range(29):
    conrad.right(3)
    conrad.forward(150)
    conrad.back(150)
    
# draw the grass
conrad.penup()
conrad.fillcolor("green")
conrad.begin_fill()
conrad.goto(-33.91,-82.97)
conrad.setheading(0)
conrad.pendown()
conrad.pencolor("green")
conrad.goto(200, -82.97)
conrad.goto(200,-200)
conrad.goto(-50,-200)
conrad.goto(-33.91,-82.97)
conrad.end_fill()

#draw flower
conrad.goto(170, -82.97)
conrad.fillcolor("brown")
conrad.begin_fill()
conrad.pencolor("black")
conrad.setheading(90)
conrad.forward(30)
conrad.left(90)
conrad.forward(5)
conrad.left(90)
conrad.forward(30)
conrad.left(90)
conrad.forward(5)
conrad.end_fill()

conrad.goto(168, -53.97)
conrad.setheading(338)

conrad.fillcolor("hotpink3")
conrad.begin_fill()
for i in range(4):
    for i in range(35):
        conrad.forward(1)
        conrad.left(4)
    conrad.right(50)
conrad.end_fill()


wn.exitonclick()