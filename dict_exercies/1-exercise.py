#!/usr/bin/python3

client = {}
print("Enter customer´s name")
client["name"] = str(input())
print("Enter customer´s last name")
client["last_name"] = str(input())
print("Enter customer´s age")
client["age"] = int(input())
print("Enter customer´s dni")
client["dni"] = str(input())
print("Enter the total amount to be paid by the customer")
client["total"] = float(input())

print(client)
