#!/usr/bin/python3


while True:
    sentence = str(input("Enter the sentence\n"))
    words = sentence.split()
    if sentence == "":
        break
    word_1, *restword, word_last = words #unpacking
    word_tuple = (word_1, word_last)
    print(word_tuple)
