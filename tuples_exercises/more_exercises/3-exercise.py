#!/usr/bin/python3

sentence = str(input("Enter the sentece\n"))
list_tuples = []


str_1 = sentence.split() #divide the sentnce into individual words
for i in range(len(str_1)):
    word = str_1[i] #store each word in the variable word
    list_tuples.append((str_1[i], len(str_1[i]), i, word[0]))
 
print(list_tuples)
