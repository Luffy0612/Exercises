#python calculator
import math
print("Opening the calculator....")
i=0
while (i==0):
    x=float(input("Enter the first number:"))
    y=float(input("Enter the second number:"))
    a='+'
    b='-'
    c='/'
    d='*'
    e='**'
    f='sqrt'
    print("+ stands for addition.")
    print("- stands for subtraction.")
    print("* stands for multiplication.")
    print("/ stands for division.")
    print("** stands for power.")
    print("sqrt stands for square root.")
    z=str(input("Enter which operation would you like to perform on x and y:"))
    if z==a:
        print(f"The sum of the numbers is {x+y}")
    elif z==b:
        print(f"The absolute difference of the numbers is {math.fabs(x-y)}")
    elif z==c:
        print(f"The division of the numbers is {round(x/y,2)}")
    elif z==d:
        print(f"The product of the numbers is {x*y}")
    elif z==e:
        print(f"{x} to the power of {y} is {pow(x,y)}")
    elif z==f:
        g=int(input("which number do you want to sware root:"))
        print(f"The suqre root of {g} is {math.sqrt(g)}")
    else:
        print("Enter a valid operation")
    h=str(input("Do you want to continue(Y/N):"))
    if h=='Y':
        i=0
    else:
        print("Shutting down the calculator...")
        break
