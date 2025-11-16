
balance = 0.0
kyc_documents= {}
def check_balance():
    global balance
    print("your Balance is ", balance)
    print("++++++++++++++++++++++++++++")

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(" amount deposited:", amt, "balance is: ", balance)
        print("++++++++++++++++++++++++++++")
    else:
        print("cant deposit a negative or zero amount")
        print("++++++++++++++++++++++++++++")

def withdraw(amount):
    global balance
    if amount <=0:
        print(" zero or negative amount entered")
        print("++++++++++++++++++++++++++++")
    elif amount > balance:
        print("Cant withdraw more than balance")
        print("++++++++++++++++++++++++++++")
    else:
        balance -= amount
        print(" amount withdrawn:", amt, "balance is: ", balance)
        print("++++++++++++++++++++++++++++")
def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("kyc not done")
    else:
        for doc in kyc_documents:
            print("kyc documents details")
            print(f"{doc}: {kyc_documents[doc]}")


if __name__ == "__main__":
    print("++++++++++++++++++++++++++++")
    print("welcome to ABC Bank")
    print("++++++++++++++++++++++++++++")
    while True:
        print("1. Check your Balance")
        print("2. Deposit an amount")
        print("3. withdraw an amount")
        print("4. CHeck KYC")
        print("5. update KYC")
        print("6. Quit")
        choice = input("Enter your Choice (1-6): ")
        print("++++++++++++++++++++++++++++")
        if choice == '1':
            check_balance()
        elif choice == '2':
            amt=float(input("Enter amount to deposit: "))
            deposit(amt)

        elif choice == '3':
            amt = float(input("Enter amount to withdraw: "))
            withdraw(amt)

        elif choice == '4':
            check_kyc()
            print("++++++++++++++++++++++++++++")
        elif choice == '5':
            kyc_docs = {}
            n_documents = int(input(" enter the number the docs you want to add: "))
            for i in range(n_documents):
                key = input("Enter the doc type: ")
                value = input("enter the document num: ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print("KYc updated")
            print("++++++++++++++++++++++++++++")
        elif choice == '6':
            print("Quitting, Have a nice day")
            break
        else:
            print("Invalid choice!")
            print("++++++++++++++++++++++++++++")

    print(" Thanks for banking with us!")
