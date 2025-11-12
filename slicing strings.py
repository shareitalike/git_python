
"""

s1 = "Hello world"
print(s1[2:7:1])
print(s1[1:12:3])

name = ("john")
age = 20
print(name,"is",age,"years old")

#Using Fstring
print(f"{name} is {age} years old")

"""
print("john \t 20")
print ("john \\20")
print ("john \n20")
print("This is python's class")
print('This is python\'s class')

sp="Python is fun"
language = "python"
version= "3.13.3"
print (language + version)
print(sp * 3,sep =' ')

#Membership in python
print("python" in sp)
print("Python" in sp)

#Comparison in strings
print("python " == "python")
#Removing spaces from string
s5= "Python"
s6 = s5.strip()
print(s6)
print(s5.strip() == "python")


#Replace
s7 = "We are Learning Python"
print(s7)
print(s7.replace("Python","java"))
print(s7.replace("e","E"))
print(s7.replace("e","E",1))

#count nad occurences
print(s7.count("Python"))
print(f"Occurences of {s5} is {s7.count(s5)}")

#Upper() and lower()
print(s7.upper())
print(s7.lower())
print(s7.title())
print(s7.capitalize())

#starting and ending
print(s7.startswith("W"))
print(s7.startswith("We are"))
print(s7.endswith("on"))


