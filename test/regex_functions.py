

import re
#sub()
s1 = "Sunday, MOnday, Tuesday, Wednesday, Sunday, Saturday"
# pat = r"Sunday"
pat = "Sunday"
replacement = "Friday"

result = re.sub(pat, replacement, s1)
print(result)
result = re.sub(pat, replacement, s1, count = 1)
print(result)

s1 = "SUnday, MOnday, Tuesday, Wednesday, Sunday, Saturday"
pat = r"S[a-z]+"
replacement = "Friday"

result = re.sub(pat, replacement, s1)
print(result)

#######################################

msg = """We are larning re, Using RE, we can search for a pattern in a given string.
Using the sub(), we can replace the pattern with a given string
"""
patt = r'\bre\b'
replacement = "Regular Expression"
result = re.sub(patt, replacement, msg)
print(result)

#ignoring the latter case
patt = r'\bre\b'
replacement = "Regular Expression"
result = re.sub(patt, replacement, msg, flags = re.IGNORECASE)
print(result)

ph = "+91-7890654321, +91-9999888765"
pat = r"[+-]"
replacement = ""
result = re.sub(pat, replacement, ph)
print(result)
