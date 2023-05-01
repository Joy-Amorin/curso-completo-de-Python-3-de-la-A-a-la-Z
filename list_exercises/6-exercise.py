#!/usr/bin/python3

word = list(input("Enter The sntence\n"))

word_p = word.copy()
word_p.reverse()

if word == word_p:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
