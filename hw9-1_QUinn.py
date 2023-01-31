def factorial(number):
    if number == 0:		
        return 1
    else:
        return number * factorial(number-1)
        
print(factorial(3))


#1
# The base case is the point at which the function stops returning the previous recursion and instead gives a certian value
#2
# if you dont use a base case your recursion will go on forever becuase it doesnt know where to stop
#3
#it runs forever because we are not reducing the number that is given to it



def sum_squares(number):
    if number == 1:
        return 1
    else:
        return number**2 + sum_squares(number -1)

print(sum_squares(5))