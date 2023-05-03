#!/usr/bin/python3

dict_k = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
print("This is the original dictionary", dict_k)

key = input("Enter the key you want to remove from the dictionary ")
if key not in dict_k:
    print(dict_k)
else:

    dict_k.pop(key)
    print("This is the update dictionary", dict_k)

