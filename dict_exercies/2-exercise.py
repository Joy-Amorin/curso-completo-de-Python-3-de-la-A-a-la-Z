#!/usr/bin/python3

subjects = {"Maths": [], "English": [],"History": [],"Science": [],"IT": []}

for key in subjects:
    print("===", key, "===")
    for i in range(1,4):
        while True:
            grade = input("Grade for the quarter {}\n".format(i))
            if not grade:
                print("Error: grade cannot empty")
            elif not grade.isdigit():
                print("Eror: grade must be a number")
            elif int(grade) > 10:
                print("Error: grade cannot be greater than 10")
            else:
                subjects[key].append(int(grade))
                break

print("\n Subject average")
for key, val in subjects.items():
    print(key, ":", sum(val)/len(val))
