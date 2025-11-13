

set1={1,13,5,67}
set2={1,4,6,67}
set3={3,4,7,6}
#union or pipeline operator
union_set= set1 | set2
print(union_set)
union_set2= set1.union(set2,set3)
print(union_set2)

#intersection, can use & operator also
common_set=set1.intersection(set2)
common_set_use= set1&set2
print(common_set_use)
print(common_set)

#common_set2= set1 + set2 #--not allowed
#minus operation for diff of sets
minus_set= set1-set2
print(minus_set)
minus_set2=set2-set1
print(minus_set2)




