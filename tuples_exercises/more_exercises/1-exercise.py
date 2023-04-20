#!/usr/bin/python3

n = int(input("Enter the numbers of integers "))
t = ()

for i in range(n):
    num = int(input("Enter the number "))
    if num % 2:
        t = (num, "odd")
    else:
        t = (num, "even")
    print(t)

