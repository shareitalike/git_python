import re

from git_python.docstrings import student_details

#using compile() so that if used multiple times then it need not waste resource
ph="aj-12345678954,vik-98764726,987654321587584"
# pat=r"\b[0-9]{7-15}" # -7-15 gives no output although no error produces
pat=r"[0-9]{7,9}"
pat_compiled = re.compile(pat)
match_obj8 = re.findall(pat,ph)
print("with ,", match_obj8)
print(pat_compiled)
print(type(pat_compiled))

#################

with open("student_details", "rt") as fh:
    data = fh.read()
print(data)
print(type(data))

phone_matches = re.finditer(pat_compiled, data)
print(phone_matches)
for matches in phone_matches:
    print(matches)

#with findall() we get a list
phone_matches = re.findall(pat_compiled, data)
print(phone_matches)
print(type(phone_matches))