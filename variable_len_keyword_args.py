
# **kwrgs -- variable length keyword arguments -- is a dictionary type


def student_details(sid, sname, **marks):
    print(marks)
    percent = sum(marks.values()) / len(marks)
    print(f"{sname} with id {sid} secured {percent}%")
student_details(101,"john",sub1=52.3,sub2=25.5,sub3=25,sub4=68)



