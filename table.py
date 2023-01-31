#table problem

# def table(rows,columns):
#     header = "*  |"
#     for column in range (1, columns + 1):
#         header = header + str(column).rjust(5)

#     print(header)
#     border = "---+" + "-----" * columns
#     print(border)
   
#     for row in range(1, rows + 1):
#         line = ""
#         for column in range(1,columns + 1):
#             line = line + str(row * column).rjust(5)
#         print(str(row).ljust(3) + "|" + line)

# table(12,12)



#lesson 7.3

# def is_prime(number):
#     for i in range(2, number):
#         if number % i == 0:
#             print(i)
#             return False  
#     return True
            

        



# print(is_prime(5))
# print(is_prime(7))
# print(is_prime(2))
# print(is_prime(713))
# print(is_prime(21))
# print(is_prime(65))
# print(is_prime(11))

import random
def check():
    guess = input("What is your guess?: ")
    pick = random.randint(1,10)
    if guess == pick:
        print("Good job")
    else:
        check()



        

print(check())
    

