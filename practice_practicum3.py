# #1
# answer = ""
# while (not answer.isnumeric()):
#     answer = input("Enter something: ")
#     #the loop will end when a number is inputed

#2
# import turtle
# wn = turtle.Screen()
# conrad = turtle.Turtle()
# y = 0
# for i in range(5):   
#     for i in range(2):
#         conrad.forward(100)
#         conrad.right(90)
#         conrad.forward(50)
#         conrad.right(90)
#     y = y - 50
#     conrad.goto(0,y)

# wn.exitonclick()   
# # 


#3
def double_consonants(word):
    new_word = ""
    for i in range(len(word)):
        
        if word[i] not in "aeiouAEIOU":
            new_word = new_word + word[i] + word[i]
        else:
            new_word = new_word + word[i]
    return new_word 

print(double_consonants("bannana"))

# #4
# def number():
#     for i in range(1,101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
        
#         else:
#             print(i)


# number()