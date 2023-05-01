#!/usr/bin/python3

str1 = str(input("Enter the first sentence\n"))
str2 = str(input("Enter the second sentence\n"))

if len(str1) != len(str2):
    print("Sentences must be the same size")
else:
    list_str = []
    for i in range(len(str1)):
        list_str.append(str1[i])
        list_str.append(str2[i])
        list_str2 = "".join(list_str)
    print(list_str2)
