def remove_dups(string):
    new_string =""
    for character in string:
        if character not in new_string:
            new_string = new_string + character
    return new_string

print(remove_dups("banana sandwich")) 