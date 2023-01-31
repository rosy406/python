# def factorial(number):
#     new_number = 1
#     for i in range(1,number+1):
#         new_number = new_number * i
#     return new_number




# def factorial(number):
#     if number == 1:      # base case
#         return 1
#     return number * factorial(number-1) # recusrion
    

    
# print(factorial(998))



def fib_sque(index):
    if index == 0:
        return 1
    elif index == 1:
        return 1
    return fib_sque(index-1) + fib_sque(index-2)


print(fib_sque(25))