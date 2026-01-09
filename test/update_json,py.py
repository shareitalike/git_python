import json
students = {'student1': {'roll': 101, 'name': 'student1', 'sports': 'hio'},
            'student2': {'roll': 102, 'name': 'student2', 'sports': False},
            'student3': {'roll': 103, 'name': 'student3', 'sports': 6},
            'student4': {'roll': 104, 'name': 'student4', 'sports': False}}

with open("students.json", "r") as f:
    data = json.load(f)
    print("here are student details", data)
data.update (students)

with open("students.json", "w") as f:
    json.dump(students, f, indent=3)
    print("student details saved")

