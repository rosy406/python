#stars
# def stars(number):
#     for i in range(1,number+1):

def stars(number):
    line = ""
    for i in range(number):
        line = line +"*"
        print(line)

stars(5)