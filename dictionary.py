

# {key1:value1, key2:value2,......}
groceries={'milk':60, 'biscuits':30}
print(groceries,type(groceries))
# dict does not have indexex
#use key to fetch values
print(groceries['milk'])
# print(groceries['eggs']) -- error as eggs are not present
#add a key and value-- if not present
groceries['eggs']=35
print("eggs added ",groceries['eggs'])
groceries['eng']=35

#dicts are mutable
groceries['milk']=65
print(groceries,type(groceries))

m={'maths':80, 'eng':75,'phy':89}
print(m)

#use get() to get the values, won't get any error if the key is not present
print(m.get("phy"))
print(m.get("chem"))
#if the key is not present to assign a default value
print(m.get("protein",100))

#membership operator
print(80 in m)
print("maths" in m)
print("not in eg ","maths" not in m)

#update to merge two dictionaries
m2= {'label tea':10, 'vitamins':20}
m.update(m2)
print(m)
#pop to delete
m.pop('phy')
print(m)

#keys can not be duplicated in dictionary, in case two same keys are present , it gives the
# latest value of the key

m2= {'label tea':10, 'vitamins':20, 'label tea':40}
print(m2)

#not allowed keys: list, set , dict -- these are mutable
#allowed keys: float, integers ,tuples are allowed but not lists --these are immutable datatypes
d1={'nine':9,'four':[1,7,9]}
print(d1)
print(d1['four'][2])
d1={'True':9,'False':4}
print(d1)
d1={(1,2,3),(4,5,6)}
print(d1,type(d1))
#value can be of any datatype
print(len(d1))

#fetch() the keys
print(m2.keys(),type(m2.keys()))
#to get only the values and another datatype created for values
print(m2.values(), type(m2.values()))
#items() gives full data as tuple presentation in print
print(m2.items(),type(m2.items()))

########### SHallow dep copy#########
import copy
l1=[1,2.5,[10,10,30],'python']
#Shallow copy
l2 = copy.copy(l1)
print(id(l1),l1)
print(id(l2),l2)
l1[1]=100
#innner element chnage in l1 can reflect in l2
l1[2][0]=11
print("with copy ",id(l1),l1)
print("with copy ",id(l2),l2)
#innner element chnage in l1 can reflect in l2 -- so use deepcopy as below
#deepcopy copies all the changes in l1 to l2
# l2=copy.deepcopy(l1)
l1[1]=101
l1[2][0]=12
l2=copy.deepcopy(l1)
print("with deepcopy ",id(l1),l1)
print("with copy ",id(l2),l2)


