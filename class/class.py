
#instance method, so first argument is self
#__init__ used to create and  initialize the attributes during the object creation

class Student(object):
    """
    This is class learning
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = 100
        print (" calling the initializer")
    def study(self, n_hours):
        print(f"Student {self.name} has {self.marks} marks and study for {n_hours} hours")
    def sports(self, n_hours):
        print("Student sports", n_hours)
#init method called automatically when object created, so pass init values
st1 = Student("John", 22)
print(st1.name)
print(st1.age)
print(st1.marks)
#printing a class object with method outputs none also
print(st1.study(10))
#so, call the class object with method directly to get rid of None
st1.sports(3)

print(st1.__dict__)
#print(st1.__getattribute__())
