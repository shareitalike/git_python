
import re
with open("student_details", "rt") as fh:
    data = fh.read()
print(data)
print(type(data))


pat = r"\b[a-zA-Z]+[a-zA-Z0-9]+[\w.-]+[@][a-z]+[.][a-z]+\b"
# pat2 = r"\b[a-zA-Z]+[a-zA-Z0-9]+[\w.-]+[@][a-z0-9]+[.][a-z]+\b"
mat_obj = re.finditer(pat, data)
for matches in mat_obj:
    print(matches)


