#A class method is defined inside the class bound to class
#use -> classmethod , to create a class method
class Welcome:
    college ="abc_college"
    depts = ["Arts", "commerce","science"]
    @classmethod
    def hello(cls):
        print("Welcome to classmethod")
        print(cls)
        print("the college called by class method ", cls.college)
    @classmethod
    def get_depts(cls):
        print(f"Dept is {cls.depts}")
    #instance methods are not bound to instance or class
    @staticmethod
    def histat():
        print("The static class method: ", Welcome.college)

    def study(self, n_hours):
        print(self)
        print(self.__class__.__name__)
        print(f"Student study for {n_hours} hours")
we1 = Welcome()
we1.hello()
we1.study(3)
we1.get_depts()
we1.histat()


