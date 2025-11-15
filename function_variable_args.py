
#*args - variable length positional arguments(0 to n)
#*nums or other variable name can be used
def add(*args):
    print(args, type(args))
    return sum(args)
result = add(10,29,30,40)
print(result)

#xargs stores values as tuple

def student_details(sid, sname,  *marks):
    percent = sum(marks) / len(marks)
    print(f"{sname} with id {sid} secured {percent}%")
student_details(101,"john",52.3,25.5,25,68,79,99,100)