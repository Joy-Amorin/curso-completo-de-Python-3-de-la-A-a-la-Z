#!/usr/bin/python3

subjects = ["Maths", "Lenguage", "History", "Computer Scince", "Music"]
grades = []

print(subjects)

s = input("Enter the subject ")

while s in subjects:
    grade = int(input("Enter a grede between 1 and 10 "))
    grades.append((s, grade))
    s = input("Enter the subject ")

    means = {"Maths": [], "Lenguage": [], "History": [], "Computer Scince": [], "Music": []}
for item in grades:
    means[item[0]].append(item[1]) #means[item[0]] accesses the list correponding to the subjects in menas dictionary

print("\n=== AVERAGE GRADES ===")

for key, val in means.items():
    print("The average grade of {} is {}".format(key, "unknown" if len(val) == 0 else sum(val) /len(val)))
    
