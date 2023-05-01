#!/usr/bin/python3

l = ["m", "a", "r", "j", "b", "g", "i", "s", "f", "g"]
print("This is the original list", l)

c = input("Enter the element you want to delete\n")

for e in l:
    if e == c:
        l.remove(e)
print(l)
