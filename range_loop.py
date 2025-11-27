#range(start,stop,step) stop is not included step default is 1

for i in range(1,11,2):
    print(i)

#reverse order print 20 to 11
for i in range(20,10,-1):
    print(i)
print("Happy New Year")

for i in range(5):
    print(i)

for i in range(0,5):
    print("zero included" ,i)

m2= {'label tea':10, 'vitamins':20, 'label tea':40}
for i in range(len(m2)):
    print(i,m2)

profits = [9,11,24,13]
for index in range(len(profits)):
    print(profits[index])
#Total , highest and lowest using loops
s=[23,45,64,76,11,21]
total = 0
for s in s:
    total=total+s
print("Total is ", total)

s1 = [11,12,34,54]
#hoghest score
highest = s1[0]
for i in s1:
    if highest < i:
        highest  = i
print("highest is ", highest)
print("s1 ",s1)
#continue and break usage : used only inside loop not outside
for num in range(10):
    if num%3 == 0:
        continue
    print(num)

for num in range(1,10):
    if num%3 == 0:
        break
    print(num)
