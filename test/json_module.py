
import json

students = {'student1': {'roll': 101, 'name': 'student1', 'sports': True},
            'student2': {'roll': 102, 'name': 'student2', 'sports': False},
            'student3': {'roll': 103, 'name': 'student3', 'sports': 6},
            'student4': {'roll': 104, 'name': 'student4', 'sports': False}}
print(students)
print(type(students))

#dump()
with open("students.json", "w") as f:
    json.dump(students, f, indent=3)
    print("student details saved")


'''
from lists import student

student = student.Student()
print(student.age)
'''