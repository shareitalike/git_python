
age = float(input("age: "))
if age < 18:
    raise ValueError("age is too young")
    print("age is too young")
#except ValueError as e:
#    print(e)

try:
    if age < 18:
        raise ValueError("age is too young")
    print("age is ok")
except ValueError as e:
    print(e)