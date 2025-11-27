
n=1 #Global variable

def fn():

    global n
    n = 5 #local variable -- will be given priority first
    # here it assigns value 5 to global variable n
    print("in fn ",n)
fn()
print(n)



