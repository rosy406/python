#lesson7-1 
# def sum_to(number):
#     '''add whole numbers up to and including the given number'''
#     answer = 0
#     for i in range(1, number + 1):          #accumulator pattern
#         answer = answer + i 
#     return answer

# print(sum_to(4))


def sum_to(endpoint):
    answer = 0
    number = 1
    while number <= endpoint:
        answer = answer + number 
        number = number + 1
    return answer 
print(sum_to(3))