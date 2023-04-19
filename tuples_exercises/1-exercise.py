#!/usr/bin/python3

n =int(input("Enter th numbers of integers  "))

number_sign = []
sign = ""

for i in range(1, n+1):
    num  = int(input("number #{} ".format(i)))
    if num > 0:
        sign = "posisive"
    elif num < 0:
        sign = "negative"
    else: 
        sign = "zero"

    number_sign.append((num, sign))
print(number_sign)

