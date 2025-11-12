
student = ["john","12","85.5"]
print(type(student))

print(student)

#slicing
l1=[3,8,1,0,4,9,7,3,6]
print(l1)
print(l1[1:6:1])
print(l1[1:6:2])

#repetition
l2=[0,5]
print(l2*3)

print(l1+l2)

# append
print(l2.append(1))
print(l2)
#insert
#syntax: list.insert(index, item)
print(l2.insert(1,3))
print(l2)
# print(l2.replace(0,2))


#extend
l2.extend([5,8])
l2.append([9,6])
print(l2)

#remove
l2.remove([9,6])
print(l2)

#pop removes element aat the index number provided
l2.pop(2)
#w/o any mention of the index last element would be deleted
l2.pop()
print(l2)

