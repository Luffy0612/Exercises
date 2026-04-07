# Number guessing game
import random
low=1
high=100
chance=0
num=random.randint(low,high)
guess=int(input("Enter a number between 1 and 100 :"))
while True:
    if guess<num:
        print("Higher!!")
        chance+=1
        guess=int(input("Enter a number again b/w 1 and 100 :"))
    elif guess>num:
        print("Lower!!")
        chance+=1
        guess=int(input("Enter a number again b/w 1 and 100 :"))
    elif guess==num:
        print("Correct!!")
        print(f"You took {chance+1} chances to guess this number.")
        break
    else:
        print("Enter a valid number!! -_-")
