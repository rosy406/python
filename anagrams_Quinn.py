#anagrams_Quinn.py
# -----------------------------------------+
# Quinn Rosenstock, Brady Terry            |  
# Computer Science, Project 7              |
# Last Updated: 12/14/2022                 |  
# -----------------------------------------|
# The code takes two inputs from a user    | 
# and then compares them to see if they are|
# anagrams.                                |
# -----------------------------------------+

import string 

#defineing function get_phrase
#gets and imput from the user and makes it all lowercase while getting rid of punctuation and spaces
def get_phrase():
    phrase = input("Enter phrase: ").replace(" ","")
    new_phrase =""
    for i in range(len(phrase)):
        if phrase[i] not in string.punctuation:
            new_phrase = new_phrase + phrase[i]
    return new_phrase.lower()


    
    
#defining anagram function
#compares the two phrases to see if they are anagrams   
    
def anagram(phrase1, phrase2):
    if len(phrase1) == len(phrase2):
        for character in phrase1:
            if phrase1.count(character) != phrase2.count(character):
                return False
        return True
            
     





#while statement that calls all of the functions 
#continues to run the function until user says no
continu = ""

while continu != "no":
    phrase1 = get_phrase()
    phrase2 = get_phrase()
    if anagram(phrase1, phrase2):
        print("The phrases are anagrams.")
    else: 
        print("The phrases are not anagrams.")
    continu = input("Do you want to continue?: ")