#!/usr/bin/python3

sentence = str(input("Enter the sentence\n"))
words = sentence.split()
list_len = []
if sentence != "":

    for i in range(len(words)):
        word_len = len(words[i])
        list_len.append(word_len)
        items = zip(words, list_len)
        dict_lists = dict(items)
    print(dict_lists)
else:
    dict_lists = {}
    print(dict_lists)
