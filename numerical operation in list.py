

#smallest number in list : use min()

l2=[2,4,7,3,1,0,8,9,-1]
print(min(l2))

print(f"smallest number: {min(l2)}")

#biggest number
print(f"biggest number: {max(l2)}")

#sum
print(sum(l2))
#nested lists

l1=[5,1.5,"python",True, None, [1,2,3],10]
''' it selects the inner list first item at the index 0'''
print(l1[-2][0])

l2=[[1,2],[3,4],[5,6,[0,1]]]
print(l2[-1])
print(l2[-1][-1])
print(l2[-1][-1][-1])


