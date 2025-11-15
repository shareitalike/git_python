
def student_details(sid, sname, **marks):
    """
    This is a docstring
    we can write what the function does here

    :param sid:
    :param sname:
    :param marks:
    :return:
    """
    print(marks)
    percent = sum(marks.values()) / len(marks)
    print(f"{sname} with id {sid} secured {percent}%")
student_details(101,"john",sub1=52.3,sub2=25.5,sub3=25,sub4=68)

print(help(student_details))

