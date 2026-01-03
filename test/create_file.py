# create file ( x mode)
fh = open("new2.txt", "xt")
#fh = open("new.txt", "rt")
# writing into the new file
fh.write("hello")
fh.write("This wAS CREATED using x mode in python")
#print(fh.read())

fh.close()
#fh.write("Test after close")