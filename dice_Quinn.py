# dice_Quinn.py
# -----------------------------------------+
# Quinn Rosenstock, Jacob Weber            |  
# Computer Science, Project 6              |
# Last Updated: 12/1/2022                  |  
# -----------------------------------------|
# This code calculates the percentage of   | 
# wins in certian number of games of craps.|
# The number of games is inputed by the    |
# user.                                     |
# -----------------------------------------+
#importing random
import random 

# function simulate_one_game(no parameters)
# returns true if game is won. False if lost
def simulate_one_game():
    #rolling dice
    roll = random.randint(1,6) + random.randint(1,6)
    #if statement that compares the dice 
    if roll == 7 or roll == 11:
     
        return True 
    elif roll == 2 or roll == 3 or roll == 12:
       
        return False 
    else:
        roll1 = 0
        # while loop that continues to roll dice until game ends
        while roll != roll1 or roll1 != 7:
            roll1 = random.randint(1,6) + random.randint(1,6)
            if roll1 == roll:
               
                return True
                 
            elif roll1 == 7:
                
                return False    

simulate_one_game()
# function get_integer(smallest valid int, largest valid int, custom message)
def get_integer(smallest_int, largest_int, message):
    smallest_int = 100
    largest_int = 5000000
    print("How many games would you like to simulate?")
    number = 0
    #while loop that makes sure number is in given range
    while number < smallest_int or number > largest_int:
        number = int(input("Enter an integer between 100 and 5000000: "))
        
    return number 

wins = 0 
games = get_integer(100, 5000000,"How many games would you like to simulate?")
#for loop that calculates the number of wins
for i in range(games):
    result = simulate_one_game()
    if result == True: 
        wins = wins + 1
#calculating percent
percent = wins / games * 100
#printing percent of wins
print("Simulated winning percentage = {:.2F}".format(percent))
