#!/usr/bin/python3

print("Enter two integers")

#n = int(input) = 2 
#list_n = []

for i in range(1):
    number = int(input("Enter number #1 " ))
    number_2 = int(input("Enter number #2 "))
    if number >= number_2:
        division = number/number_2
        rest = number % number_2
        list_n = [number, number_2, int(division), rest]
        list_n_t = tuple(list_n)
        print(list_n_t)
    else:
        print("The first number must be greater or equal to sencond number")

