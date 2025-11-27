
#1. BAse condition
#2 exit condition
#3 recursive condition


def fact_rec(num):
    if num==0:
        return 1
    else :
        factorial=num * fact_rec(num-1)
        return factorial
print(fact_rec(5))


