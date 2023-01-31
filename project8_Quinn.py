# --------------------------------------
# Computer Science, Project 8
# January __, 2022
# Your Name
# --------------------------------------

def count_vowels(sentence):
    vowels = 0
    for char in "aeiou":
        vowels += sentence.count(char)
    return vowels
    

def count_vowels_iterative(sentence):
    vowels = 0 
    for i in range (len(sentence)):
        if sentence[i] in "aeiou":
            vowels += 1
    return vowels

def count_vowels_recursive(sentence):
    pass

# --------------------------------------

answer = "yes"
while (answer == "yes") or (answer == "y"):
    sentence = input("Please enter a sentence to evaluate: ")
    sentence = sentence.lower()     # convert to lowercase
    print()
    print("Number of vowels using count     =", count_vowels(sentence))
    print("Number of vowels using iteration =", count_vowels_iterative(sentence))
    # print("Number of vowels using recursion =", count_vowels_recursive(sentence))
    print()
    answer = input("Would you like to continue: ").lower()
    print()