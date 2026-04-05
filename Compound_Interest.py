#python compound interest calculator
import math
while True:
    p=float(input("Enter the initial Principal Amount (in dollars):"))
    r=float(input("Enter the interest rate per year:"))
    t=float(input("Enter the time elapsed (in years):"))
    if p<0:
        print("How can the principal amount be negative IDIOT!!")
    elif r<0:
        print("The rate of interest cant be neative :(")
        break
    elif t<0:
        print("WOw your time is negative XD!!")
        break
    else:
        None
    compound=p*((1+(r/100))**(t))
    print(f"Your Balance after {t} year/s is {compound:.2f}")
    break
