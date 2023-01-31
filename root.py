#root.py

#define variables

#calculates roots

#output results

a = 1
b = 1
c = -6

first_x = (-b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
second_x = (-b - (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
print("x equals", first_x,"or", second_x)