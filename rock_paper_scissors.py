# Stone Paper Scissor program
import random
print("Welcome to Stone!! Paper!! Scissors!! game X).... ")
x=['stone','paper','scissor']
print("There are two modes:- \n Warrior -----> The game will continue endlessly until you've won!! \n commoner ----> it will have rounds by your choice, if you want to continue or not. ")
y=input("which mode do you want to choose ( Warrior / commoner ) :")
if y.lower()=='warrior':
    i=0
    chance=0
    while i==0:
        b=random.choice(x)
        guess=input("Enter your choice ( Stone , Paper , Scissor ) : ")
        if guess.lower()=='stone':
            if b=='paper':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("You've Lost!!")
                chance+=1
                i=0
            elif b=='scissor':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("You've Won!!")
                print(f"You have taken a total of {chance+1} chance(s)")
                continue_choice=input("Do you want to continue (Y/N) : ")
                if continue_choice=='N':
                    print("Sacred huh XD.....")
                    i=1
                elif continue_choice=='Y':
                    print("Thats the spirit!!")
                    i=0
                else:
                    print("Enter a valid choice IDIOT -_-")
            elif b=='stone':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("Draw!!")
                chance+=1
                i=0
            else:
                print("Enter a valid input -_-")
                i=0
        if guess.lower()=='paper':
            if b=='paper':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("Draw!!")
                chance+=1
                i=0
            elif b=='scissor':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("You've lost!!")
                i=0
                chance+=1
            elif b=='stone':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("You've won!!")
                print(f"You have taken a total of {chance+1} chance(s)")
                continue_choice=input("Do you want to continue (Y/N) : ")
                if continue_choice=='N':
                    print("Sacred huh XD.....")
                    i=1
                elif continue_choice=='Y':
                    print("Thats the spirit!!")
                    i=0
                else:
                    print("Enter a valid choice IDIOT -_-")
            else:
                print("Enter a valid input -_-")
                i=0
        if guess.lower()=='scissors':
            if b=='stone':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("You've Lost!!")
                chance+=1
                i=0
            elif b=='paper':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("You've Won!!")
                print(f"You have taken a total of {chance+1} chance(s)")
                continue_choice=input("Do you want to continue (Y/N) : ")
                if continue_choice=='N':
                    print("Sacred huh XD.....")
                    i=1
                elif continue_choice=='Y':
                    print("Thats the spirit!!")
                    i=0
                else:
                    print("Enter a valid choice IDIOT -_-")
            elif b=='scissors':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("Draw!!")
                chance+=1
                i=0
            else:
                print("Enter a valid input -_-")
                i=0
elif y.lower()=='commoner':
    c=int(input("How many rounds do you want to have: "))
    for z in range(c):
        b=random.choice(x)
        guess=input("Enter your choice ( Stone , Paper , Scissor ) : ")
        if guess.lower()=='stone':
            if b=='paper':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("You've Lost!!")
            elif b=='scissor':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("You've Won!!")
            elif b=='stone':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("Draw!!")
            else:
                print("Enter a valid input -_-")
        if guess.lower()=='paper':
            if b=='paper':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("Draw!!")
            elif b=='scissor':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("You've lost!!")
            elif b=='stone':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("You've won!!")
            else:
                print("Enter a valid input -_-")
        if guess.lower()=='scissors':
            if b=='stone':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("You've Lost!!")
            elif b=='paper':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("You've Won!!")
            elif b=='scissors':
                print(f"Computer's choice : {b:10}")
                print(f"Your choice : {guess:10}")
                print("Draw!!")
            else:
                print("Enter a valid input -_-")
