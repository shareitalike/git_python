
#instance method, so first argument is self
#__init__ used to create and  initialize the attributes during the object creation


class Student(object):
    """
    This is class learning
    """
    # class variables are inside the class not in init
    #the class variables are shared to all objects
    college ="abc_college"
    depts = ["Arts", "commerce","science"]

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
print(st1.depts)
#printing a class object with method outputs none also
print(st1.study(10))
#so, call the class object with method directly to get rid of None
st1.sports(3)

#__dict__ only shows the instance variables not class variables
print(st1.__dict__)
#print(st1.__getattribute__())
#help(Student)

st2 = Student("alice", 24)
print(st1.depts)
st1.sports(5)
print(st1.college)
print(st1.depts)