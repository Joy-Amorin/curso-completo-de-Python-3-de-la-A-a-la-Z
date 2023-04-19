#!/usr/bin/python3

num = int(input("Enter a number from 1 to 10 (0 to exit) "))

while num != 0:
    grade = ""

    if num < 1:
        print("Enter a number from 1 to 10 (0 to exit) ")
    if num < 5:
        grade = "suspense"
        print((num, grade))
    elif num < 7:
        grade = "approved"
        print((num, grade))
    elif num < 9:
        grade = "notable"
        print((num, grade))
    elif num <= 10:
        grade = "excellent"
        print((num, grade))
    else:
        print("Enter a number from 1 to 10 (0 to exit)" )
    num = int(input("Enter a number from 1 to 10 (0 to exit "))
        
