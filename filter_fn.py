

#filter(function,sequence)

seq= {1,2,3,4,5}
odd = lambda x:True if x % 2 !=0 else False
filtered_output=filter(odd, seq)
print("first",filtered_output)

#above code merged into one line
seq= {1,2,3,4,5}
#use filter to keep selected condition fulfilled results
filtered_output=filter(lambda x:True if x % 2 !=0 else False, seq)
#use map to store all results even if it is false
mapped_output=map(lambda x:True if x % 2 !=0 else False, seq)

print(filtered_output)
print(mapped_output)
print("odd numbers are", list(filtered_output))
print("odd numbers are in map", tuple(mapped_output))
print("odd numbers are", list(mapped_output))
#usually map is not used in these type of sequences, used in below way:
#map iterates through all the elements of the element ans stores output according to the condition
mapped_output2=map(lambda x:x**2 , seq)
print(mapped_output2)
print("odd numbers are in map", tuple(mapped_output2))
