"""compile error => syntax error and compile error
2. Exception or runtime error --during execution
    built in exceptions - by python itself like name error, value error
    for manual exception use try, except block

"""

#multiple except block can be there in a try block
try :
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter another number : "))
    res = num1 / num2
    print(res)
except ZeroDivisionError:
    print("division by zero")
#except ValueError: # if valueerror builtin is not used and other than digit passed then,
    # it will give error
#    print("input only digits")
except IndexError:
    print("index error")
except (ZeroDivisionError, TypeError) as e:
    print(e)
#“except Exception is safer than except: because it excludes system-exiting exceptions.”
except Exception as e:
    print("Unexpected error:", e)


'''
try :
    res = num1 / num2
    print(res)
except:
    print("denominator can't be zero")
'''