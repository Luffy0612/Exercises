#Banking program
import time
def deposit():
    x=float(input("Enter the amount to be deposited : $"))
    return x
def withdraw():
    y=float(input("Enter the amount to withdraw : $"))
    return y
balance=0
print("Welcome to SDFC bank account help center.")
while True:
    print('************************')
    print("1. Withdraw money \n2. Deposit money \n3. Check Balance \n4. Exit ")
    print('************************')
    choice=int(input("What service would you like to avail : "))
    print('************************')
    if choice==1:
        x=withdraw()
        if x>balance:
            print('************************')
            print("Insufficient Balance...")
        else:
            balance-=x
            print('************************')
            print(f"You have succesfully withdrawn ${x} from your bank account. ")
    elif choice==2:
        y=deposit()
        balance+=y
        print('************************')
        print(f"You have succefully deposited ${y} in your bank account.")
    elif choice==3:
        print('************************')
        print(f"You have a total of ${balance} as of {time.strftime("%x %X %p",time.localtime())} ")
    elif choice==4:
        print('************************')
        print("Thank you for choosing our services....")
        print('************************')
        break
