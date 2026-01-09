
import json
import pickle
students = {'student1': {'roll': 101, 'name': 'student1', 'sports': 'hio'},
            'student2': {'roll': 102, 'name': 'student2', 'sports': False},
            'student3': {'roll': 103, 'name': 'student3', 'sports': 6},
            'student4': {'roll': 104, 'name': 'student4', 'sports': False}}

#serialization - using pickle, opening in b mode is mandatory
with open("students.bin", "wb") as fh:
    pickle.dump(students, fh)
    print("here are student details pickled")

with open("students.bin", "rb") as f:
    data = pickle.load(f)
    print("here are student details displayed using pickle load\n", data)

with open("students.bin", "rb") as f:
    data = pickle.load(f)
    print(type(data), data)
    data2 = pickle.load(f)
    print("here are student details displayed using pickle load\n", data2)

