#!/usr/bin/python3

n = int(input("How many point will you introduce? "))
points = []

for i in range(n):
    x = float(input("Indicates the x-coordinate "))
    y = float(input("Indicates th y-coordinates "))

    if x >= 0 and y >= 0:
        quadrant = "I"
    if x <= 0 and y >= 0:
        quadrant = "II"
    if x <= 0 and y <= 0:
        quadrant = "III"
    if x >= 0 and y <= 0:
        quadrant = "IV"
    if x == 0 and y == 0:
        quadrant = "center"

    points.append((x, y, quadrant))

for point in points:
    x, y, quadrant = point #unpacking
    print("Thoe point ({}, {}) belongs to quadrant {}".format(x, y, quadrant))
