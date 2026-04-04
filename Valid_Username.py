#validate user input
#username is no more than 12 characters long
#username must not contain spaces
#username must not contain digits
name=str(input("Enter your valid name:"))
a=len(name)
b=name.isalpha()
if (a<13):
    if (b==True):
        print("It is a valid name :)")
    else:
        print("The name is invalid !! \nLit should not contain any spaces or digits!!")
else:
    print("The name is invalid!! \nIt should be no more than 12 characters!!")
