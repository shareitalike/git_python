

t1=("python",10,1.5,True,[1,2,4],(10,20))
print(len(t1))
print(type(t1))
print(t1[-1])

t2=10,20,30
print(t2)
print(type(t2))
# t2=list(t2)
# print(t2,type(t2))
print(t1+t2)

#Membership operation: in or not in
print(10 in t2)
print(10 not in t1)

#count of element
print(t2.count(10))
#index of the provided element
print(t2.index(10))

#min,max,sum
print(sum(t2))
print(min(t2))
print(max(t2))

#immutability and mutabiity
#lists are mutable, tuples and strings are immutable
s1= "Python is fun"
s2=s1.replace("Python","java")
print(s2)
print(s1)

#lists are mutable
l1=[12,34,54]
print(id(l1))
l1.append("banana")
print(l1)
print(id(l1))
l1[-1]=13
print(l1)
#


