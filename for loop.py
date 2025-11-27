
l=['mike',10.2,19]

for x in l:
    print(x)
j='apple'
for x in j:
    print(j)
#using range
# for x in range(1_11):
    print(x)
#correct for loop range
for x in range(1,11):
    print(x)
#for loop print keys not values as below in dict
m2= {'label tea':10, 'vitamins':20, 'label tea':40}
for i in m2:
    print(i)
    print(i,m2[i]) #to print keys and values both
for i in m2.items():
    print(i)
    print("to print values other way not as tuple",i[0],i[1])
