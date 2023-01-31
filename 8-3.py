#lesson8-3.py
def find(phrase, letter):
    index = -1
    for i in range(len(phrase)):
        if phrase[i] == letter:
            index = i
            return index 

            

    return index


def count(phrase, letter):
    times = 0 
    for charecter in phrase:
        if charecter == letter:
            times += 1

    return times



print(count("Griffins","f"))


# print(find("Griffins", "f"))
# print(find("Griffins","z"))