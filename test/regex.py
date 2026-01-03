
#Regex- Regular expression re module contains functions
import re


mes = "The current python is 3.13"
print("python" in mes)
print("the start place of the string: ", mes.find('3.13'))
print(mes.find('python'))

match_obj = re.search('13', mes)
print(match_obj)

if re.search('13', mes):
    print("found")
else:
    print("not found")

print(mes[24])
# re.search((regex_pattern), string) - return match objects else none


match_object = re.search("[0-9][0-9]", mes)
match_object2 = re.search("[013][0-9]", mes)
print(match_object)
print(match_object2)
match_object2 = re.search("[0-9][0-9]", "HOuse number: 251")
print(match_object2)

# getting dot(.) also matched as below -- dot(.) matches any character except new line char(\n)
match_object3 = re.search("[0-9].[0-9][0-9]", mes)
print(match_object3)
match_object3 = re.search("[0-9].[0-9]", mes)
print(match_object3)

match_object2 = re.search("[0-9].[0-9]", "HOuse number: 251")
print(match_object2)

match_object2 = re.search("[0-9][.][0-9]", "HOuse number: 251")
print(match_object2)
#if . is in [] then it checks for exact match . as meta characters
match_object2 = re.search("[0-9][.][0-9]", mes)
print(match_object2)

s1 = "python is a programming language"
#[A-Z],[a-z]
pat = r"[A-Z][a-z]"
pat2 = r"[a-z][a-z]"
match_object2 = re.search("[A-Z][a-z]", s1)
match_object3 = re.search(pat, s1)
match_object4 = re.search(pat2, s1)
print(match_object2)
print(match_object3)
print(match_object4)

#in the following the \n will not be taken as new line if we use r
pat = r"old\new"
print(pat,"with r new line is not printed")

pat = "old\new"
print(pat,": without r, new line is printed")

# \d --- any 1 digit character
s4 = "python is a programming language"
pat = r"[a-z]{8}"
match_obj4=re.search(pat,s4,)
print(match_obj4)
# ^ - caret - only at the beginning of the string
pat = r"^[a-z]{8}"
match_obj4=re.search(pat,s4,)
print("caret",match_obj4)
#\D -- any character other than digit

# $ - end of the string match(opposite of caret)
pat = r"[a-z]{8}$"
match_obj4=re.search(pat,s4,)
print("dollar",match_obj4)

#group - () + | (or)
emails="abc_123@example.com random words and characters. x1y2z3.abc.edu"
pat=r"(com|edu)"
match_obj=re.search(pat,emails)
print(match_obj,"group verify")


s7 = " We are learning regex in python"
# pat = r"[A-Z]{a-z}"
pat = r"[A-Z][a-z]"
match_obj7 = re.search(pat,s7)
print(match_obj7)
#match() function
match_obj7 = re.match(pat,s7)
print("search and match diff ",match_obj7)
#####################################################
import re

text = "Hello World"

# Match only at the beginning
result = re.match("Hello", text)
print(result)   # ✅ Match object

result = re.match("World", text)
print(result)   # ❌ None (because "World" is not at the start)

import re

text = "Hello World "

# Search anywhere in the string
result = re.search("World", text)
print(result)   # ✅ Match object

result = re.search("Python", text)
print(result)   # ❌ None (not found)
#############################################################

match_obj7 = re.findall(pat,s7)
print(match_obj7)

#limit 4-max 6 words (except spaces, if a space is there it searches again for 4-6 letters)
pat = r"[a-z]{4,6}"
match_obj7 = re.findall(pat,s7)
print(match_obj7)
#{4,} - limit (at leat 4) 4 to max as many words (except spaces if a space is there
# it searches again for 4- as many words)
pat = r"[a-z]{4,}"
match_obj7 = re.findall(pat,s7)
print(match_obj7)

ph="aj-12345678954,vik-98764726,987654321587584"
pat=r"\b[0-9]{7,9}"
match_obj8 = re.findall(pat,ph)
print("with comma",match_obj8)


pat=r"[0-9]{7,9}"
match_obj8 = re.findall(pat,ph)
print("with comma",match_obj8)
#same as above with 7-9, hyphen in between instead of comma, no output
pat=r"\b[0-9]{7-15}"
match_obj8 = re.findall(pat,ph)
print("with -", match_obj8)

pat=r"[0-9]{7,11}"
match_obj8 = re.findall(pat,ph)
print(match_obj8)

#with \b - boundary means exact that many words from the end(if contains more letters)
pat=r"[0-9]{7,9}\b"
match_obj8 = re.findall(pat,ph)
print("boundary at end",match_obj8)

#e.g- "\b[0-9]{7,11}\b"  - means -exact 7 to 11 numbers containing strings would be matched
pat=r"\b[0-9]{7,9}\b"
match_obj8 = re.findall(pat,ph)
print("bothe boundaries",match_obj8)

#finditer() - takes out all the occurrences in iterable and shows as re.match objects
pat=r"\b[0-9]{7,11}\b"
match_obj_iter = re.finditer(pat,ph)
print(match_obj_iter)
for match in match_obj_iter:
    print(match)



