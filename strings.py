#lesson8-1.py
import string

# def count_vowels(message):
#     vowels = 0
#     for i in range(len(message)):
#         if message[i].lower() in "aeiou":
#             vowels = vowels + 1
#     return vowels 


#            # for charecter in message:
#     #     if charecter in "AEIOUaeiou":
#     #         vowels = vowels + 1


# print(count_vowels("Petra Acadeny"))

def extract(letter, message):
    new_string = 0 

    for i in range(len(message)):
        if message[i] != letter :
            new_string = new_string[:i] + message[i+1:]


    return new_string





print(extract("a", "bannana"))