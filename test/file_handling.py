

#Modes(r, x, w, a, t, b => rt is the default mode)
file_handler = open("practice.txt", "rt")
print(file_handler.read())
print(file_handler)

#closing a file
#file_handler.close()

# w mode overwrites the contents of the existing file. changes are permanent
#if file does not exit , w mode creates a new file
fh = open("practice2.txt", "wt")
fh.write(" this is done using w mode \n and this is line 2 \n this is line 3")
fh.write(
    "\nthis is done using a mode\n"
    "printed using append mode\n"
    "a modes create the file also\n"
    "if it is not present\n"
)
fh.close()

#now open for reading
fh = open("practice2.txt", "rt")
content = fh.read()
fh = open("practice2.txt", "rt")
content1 = fh.read(10)
print(f"content printing : {content}")
fh.seek(0)  # 🔥 reset cursor to beginning
print(f"the content1 is : {content1}")
#read line1, line2 and line3
line1 = fh.readline()
line2 = fh.readline()
line3 = fh.readline()
print(f"line1: {line1}")
print(f"line2: {line2}")
print(f"line3: {line3}")

#readlines() gives each line including new lines but readline gives only single line
#professional python code example
with open("practice2.txt", "rt") as fh:
    lines = fh.readlines()
print(f"all lines are: {lines}")
print(type(lines))

with open("practice2.txt", "rt") as fh:
    lines = fh.read()
print(f"read command outputs are: {lines}")

#closing a file
file_handler.close()
print(file_handler)

#can close multiple times:
file_handler.close() # but no need to do it

