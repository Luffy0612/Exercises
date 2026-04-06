# Python Quiz program
score=0
i=0
while True:
    quests=['1. What is the output of len("Python")?',
            '2. Which keyword is used to define a function in Python?',
            '3. What data type is the result of 3 / 2 in Python?',
            '4. Which of these is a mutable data type?',
            '5. Which symbol is used for comments in Python?']
    gueses=[]
    answers=['B','B','B','C','B']
    options=(('A. 5','B. 6','C. 7','D. 8'),
            ('A. func','B. def','C. function','D. define'),
            ('A. int','B. float','C. str','D. bool'),
            ('A. tuple','B. string','C. list','D. int'),
            ('A. //','B. #','C. /*','D. --'))
    for x in range(len(quests)):
            print("----------------------------------")
            print(quests[x])
            print("Options:-")
            for y in range(len(options[x])):
                    print(options[x][y])
            h=input("Enter your answer ( A , B , C , D ): ")
            gueses.append(h)
            if h.upper()==answers[x]:
                    print(f"{h} is the correct answer!!")
                    score+=1
            else:
                print(f"{h} is Incorrect... {answers[x]} is the correct answer.")
    print("===============================")
    print("           Results             ")
    print("===============================")
    print(f"Total score = {score}/5")
    print("Guesses = ", end="")
    for x in (gueses):
          print(x, end=" ")
    print("\n", end="")
    print("Answers = ",end="")
    for x in (answers):
          print(x, end=" ")
    print("\n", end="")
    if score>=3:
        print("Congrats you passed!!")
        break
    else:
        print("Aww you failed...")
        g=input("Would you like to Try again(Y/N):")
        if g=='N':
            print("You should try.... -_-")
            break
