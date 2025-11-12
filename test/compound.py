
principal =float(input("Enter Princ: "))
rate =float(input("Enter rate: "))
time =float(input("Enter time: "))
#amount = principal * (1 + rate/100) ** time
amount = principal * pow((1+rate/100),time)
ci= amount-principal
print("compound interest: ", ci)