# dice game

import random

print("dice game start")
while True:
    choice= input("Press 'Enter' to roll a dice or 'q' to quit")
    choice=choice.strip()
    if choice=='q':
        print("Game off")
        break
    elif choice == '':
        number=random.randint(1,6)
        print(f"your number is {number}")
    else:
        print("invalid input")
