#lesson 6-1 

email = "quinnrosenstock@gmail.com"
password = "quinn"
# inputpass = input("what is your password: ")
def passw():
    inputpass = input("what is your password?: ")
    if inputpass == password:
        inputemail = input("what is your email?: ")
        if email == inputemail:
            print("good job")
        else:
            print("wrong email")
            passw()
    elif inputpass == "quin":
        print("your gay")
        passw()
    else:
        print("wrong password")
        passw()
    return inputpass

passw()
   

# def grade(score):
#     if score >= 90:
#         letter_grade = "A"
#     elif score >= 80 and score < 90:
#         letter_grade = "B"
#     elif score >= 70 and score < 80:
#         letter_grade = "C"
#     elif score >= 60 and score < 70:
#         letter_grade = "D"
#     elif score < 60:
#         letter_grade = "F"
    
#     return letter_grade

# print(grade(70))
















