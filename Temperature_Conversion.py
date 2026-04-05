#Temperature Conversion calculator
#problem- to repeat the program if the entered unit is invalid 
i=0
print("Opening the temperature converison calculator....")
while i==0:
    print("You want to convert temperature")
    units=['Celsius','fahrenheit','Kelvin']
    From=input(f"From {units}:")
    if From not in units:
        print("Enter a valid unit!!")
        break
    To=input(f"To {units}:")
    if To not in units:
        print("Enter a valid unit!!")
        break
    a=float(input(f"Enter the Temperature in {From}:"))
    if From=='Celsius':
        if To=='Celsius':
            print(f"Temperature coverted is {a} {To}")
        elif To=='fahrenheit':
            print(f"Temperature converted is {(9/5)*a +32} {To}")
        elif To=='Kelvin':
            print(f"Temperature converted is {a + 273} {To}")
        else:
            print("Enter a valid unit !!")
    elif From=='fahrenheit':
        if To=='Celsius':
            print(f"Temperature coverted is {(5/9)(a-32)} {To}")
        elif To=='fahrenheit':
            print(f"Temperature converted is {a} {To}")
        elif To=='Kelvin':
            print(f"Temperature converted is {((a-32)/(1.8))+273} {To}")
        else:
            print("Enter a valid unit !!")
    elif From=='Kelvin':
        if To=='Celsius':
            print(f"Temperature coverted is {a-273} {To}")
        elif To=='fahrenheit':
            print(f"Temperature converted is {(9/5)(a-273)+32} {To}")
        elif To=='Kelvin':
            print(f"Temperature converted is {a} {To}")
        else:
            print("Enter a valid unit !!")
    else:
        print("Enter a valid unit!!")
    h=input("Do you want to conitnue (Y/N):")
    if h=='Y':
        i=0
    else:
        print("Closing the Temperature conversion calculator...")
        break
