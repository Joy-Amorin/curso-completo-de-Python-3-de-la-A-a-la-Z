#!/usr/bin/python3
from math import pi
radians_t = ()

while True:
    user_input = (input("Enter numbers between 0 and 360 \n"))
    if user_input == "":
        break
    n = int(user_input)
    if n <= 360:
        radians = n * pi/180
        radians_t = (n, radians)
        print(radians_t)
        
    else:
        break
