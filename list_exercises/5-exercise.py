#!/usr/bin/python3

sentence = input("Enter the sentence\n")
sentence = sentence.lower()
consonants = []

vowels = "aeiou"
for c in sentence:
    if c.isalpha() and c not in vowels:
        if c not in consonants:
            consonants.append(c)
print(consonants)


  
