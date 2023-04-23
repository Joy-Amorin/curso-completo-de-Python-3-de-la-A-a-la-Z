#!/usr/bin/python3


while True:
    sentence = str(input("Enter the sentence\n"))
    words = sentence.split()
    if sentence == "":
        break
    word1, *restword, word_l = words #unpacking
    word_tuple = (word1, word_l)
    print(word_tuple)
