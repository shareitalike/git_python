

set1={1,13,5,67}
set2={1,4,6,67}
set3={3,4,7,6}
#add function
set1.add(5)
set1.remove(1)
#to avoid errors if the element is not present use discard
set1.discard(13)

#union or pipeline operator
union_set= set1 | set2
print(union_set)
union_set2= set1.union(set2,set3)
print(union_set2)

#intersection, can use & operator also#frozen sets

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

#frozen sets are immutable, like add, remove, discard not allowed
fs1=frozenset({10,20,30})
fs2=frozenset({1,2,30})
print(fs1, type(fs1))
print( fs1-fs2)

print(fs1 | fs2)



