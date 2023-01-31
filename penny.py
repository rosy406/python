#penny.py

# user input
number_of_pennies = input("how many pennies do you have?: ")
number_of_pennies = int(number_of_pennies)

# calculation
number_of_nickels = number_of_pennies // 5
number_of_pennies_left = number_of_pennies % 5


#print statement
print(" you have", number_of_nickels,"nickels", "and", number_of_pennies_left, "pennies")