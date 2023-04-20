#!/usr/bin/python3

year = int(input("Enter a year "))

chine_zodiac = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]

index = (year - 1900) % 12

zodiac = (year, chine_zodiac[index])

print(zodiac)
