

import random
print(random.random())
#randint(a,b) -- returns random int bet a and b including a and b
print(random.randint(10,30))
#choice(n)
n=[45,23,11,2,3,4]
print(random.choice(n))
#shuffle(sequence) -- returns the elements shuffled in random order
f=["arc","guava","elo","higo"]
random.shuffle(f)
print(f)

