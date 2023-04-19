#!/usr/bin/python3

s = input("Enter de sentence\n")
s = s.lower()

vowels = ["a", "e", "i", "o", "u"]
vowels_count = 0
consonants_count = 0
blank_count = 0

for c in s:
    if c in vowels:
        vowels_count += 1
    elif c.isalpha():
        consonants_count += 1
    elif c == " ":
        blank_count += 1

info = [("vowels", vowels_count), ("consonants", consonants_count), ("blank", blank_count)]
print(info)
