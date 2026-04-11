#Hangman Game
import random
import string
i=0
def rain():
    print("*****************")
    print("   HangMan Game  ")
    print("*****************")
    strings=['PEACH','MELON','GRAPE','FRUIT','PRUNE','APPLE','BANANA','GUAVA','PINEAPPLE','ORANGE','WATERMELON']
    hang_man={0:["----------+",
            "          |",
            "          |",
            "          |",
            "          |",
            "          |",],
        1:["----------+",
            " |        |",
            "          |",
            "          |",
            "          |",
            "          |",],
        2:["----------+",
            " |        |",
            " O        |",
            "          |",
            "          |",
            "          |",],
        3:["----------+",
            " |        |",
            " O        |",
            " |        |",
            "          |",
            "          |",],
        4:["----------+",
            " |        |",
            " O        |",
            "/|        |",
            "          |",
            "          |",],
        5:["----------+",
            " |        |",
            " O        |",
            "/|\\       |",
            "          |",
            "          |",],
        6:["----------+",
            " |        |",
            " O        |",
            "/|\\       |",
            "/         |",
            "          |",],
        7:["----------+",
            " |        |",
            " O        |",
            "/|\\       |",
            "/ \\       |",
            "          |",]}
    for i in range(len(hang_man.get(0))):
            print(hang_man.get(0)[i])
    print("*****************")
            
    word=random.choice(strings)
    Word=list(word)
    guesses=[]
    guesses_ss=set()

    for x in range(len(Word)):
        guesses.append("__ ")
    a=1
    while True:
        guess=input("Guess a letter: ")
        if guess.isalpha():
            if guess in guesses_ss:
                print("You already guessed this letter -_-")
                continue
            else:
                guesses_ss.add(guess)        
            if guess.upper() in Word:
                for i in range(len(Word)):
                    if Word[i]==guess.upper():
                        guesses[i]=Word[i]
                print(*guesses)
                print("Correct!!")
                if word==("".join(guesses)):
                    print("You Won!!")
                    h=input("Do you want to play again (Y/N): ")
                    if h=='Y':
                        rain()
                    elif h=='N':
                        print("See you next time..")
                        i+=1
                        break                    
                else:
                    pass
            else:
                print("Oops...")
                for i in range(len(hang_man.get(a))):
                    print(hang_man.get(a)[i])
                print(*guesses)
                a+=1
                if a==8:
                    print("You lost...")
                    print(f"Correct Answer: {word}")
                    h=input("Do you want to play again (Y/N): ")
                    if h=='Y':
                        pass
                    elif h=='N':
                        print("Better Luck next time..")
                        break
        else:
            print("Enter a valid letter!!")
if i==0:
    rain()
