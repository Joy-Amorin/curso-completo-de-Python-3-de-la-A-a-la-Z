#!/usr/bin/python3


while True:
    sentence = input(str("Enter the sentece\n"))
    if sentence != "":
        len_sentence = len(sentence.replace(" ", "")) #removing space
        words = sentence.split()
        words.append(len_sentence) #add numbers of characters to list
        word_tuple = tuple(words) #convert the list to tuple
        print(word_tuple)
    else:
        break

