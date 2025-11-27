
'''
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
'''

for i in range(1,6):
    for j in range(1,i+1):
        print('*', end=' ')
    print()
#problem in the below code
for i in range(1,6):
    for j in range(1,i+1):
        print('i', end=" ")
    print()



