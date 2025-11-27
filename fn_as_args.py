
#fn as arguments of another fn

def add(num):
    return num+1
print(add(10))

def sq(num):
    return num ** 2
print(sq(10))

num1=int(input("enter number"))
res_1 = add(num1)
res_2 = sq(num1)
#fn within function
print("output is ",sq(add(num1)))

