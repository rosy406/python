#1 
# def rabbit_ears(number):
#     new_string = 0 
#     for i in range(number):
#         if i % 2 == 0:
#             new_string = new_string + 2
#         else:
#             new_string = new_string + 1
#     return new_string




# print("Total number of ears:",rabbit_ears(10))


#2
# import turtle as t
# wn = t.Screen()
# conrad = t.Turtle()
# wn.bgcolor("green")
# conrad.color("red")
# conrad.pensize(5)
# for i in range(4):
#     for i in range(4):
#         conrad.forward(100)
#         conrad.left(90)
#     conrad.left(90)

# conrad.hideturtle()


#3
# import random 
# sides = random.randint(4,12)
# angle = 180 - (((sides - 4) * 180 + 360) / sides)
# wn.bgcolor(random.random(),random.random(),random.random())
# conrad.color(random.random(),random.random(),random.random())
# for i in range(sides):
#     conrad.forward(90)
#     conrad.right(angle)



#4
# def anti_first_amendment(sentance):
#     new_sentance = ""
#     for i in range(len(sentance)):
#         if sentance[i] not in "lmnopeLMNOPE":
#             new_sentance += sentance[i]
#     return new_sentance


# print(anti_first_amendment("My name is Ella Minnow Pea"))



#5 
# def replace1(word,letter,replacement):
#     new_string = ""
#     for i in range(len(word)):
#         if word[i] == letter:
#             new_string += replacement
#         else: 
#             new_string += word[i]
#     return new_string

# print(replace1("loon","l","m"))

def pig_latin(word):
    new_word = ""
    if word[0] not in "aeiouAEIOU":
        new_word = word.replace(word[0], '') + word[0] + 'ay'
    else:
        new_word = word + 'ay'
    return new_word

print(pig_latin("joemamma"))
print(pig_latin("apple"))











# wn.exitonclick()


