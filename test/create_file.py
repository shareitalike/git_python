# create file ( x mode)
fh = open("new2.txt", "xt+")
#fh = open("new.txt", "rt")
# writing into the new file
fh.write("hello\n")
fh.write("This wAS CREATED using x mode in python")
#print(fh.read())

fh.close()
#fh.write("Test after close")

#opening a file in w mode overwrites the file with blanks, then if
#it is read the file returns blanks
