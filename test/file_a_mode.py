
# a mode - add new content at the end of the file
fh = open("practice2.txt" , 'at')
fh.write(
    "\nthis is done using a mode\n"
    "printed using append mode\n"
    "a modes create the file also\n"
    "if it is not present\n"
)
fh.close()

fh = open("practice2.txt" , 'rt')
content = fh.readlines()
print(f"content printing : {content}")