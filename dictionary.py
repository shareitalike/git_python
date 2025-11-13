

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
#pop
m.pop('phy')
print(m)

#keys can not be duplicated in dictionary, in case two same keys are present , it gives the
# latest value of the key

m2= {'label tea':10, 'vitamins':20, 'label tea':40}
print(m2)
