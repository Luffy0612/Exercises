#Weight converter for kg,
i=0
print("Opening the Weight Calculator...")
while i==0:
    print("You want to convert weight")
    units=['kg','mg','g','ton','stone','pounds']
    From=input(f"From {units}:")
    To=input(f"To {units}:")
    a=float(input(f"Enter the weight in {From}:"))
    if From=='kg':
        if To=='kg':
            print(f"{a} kgs")
        elif To=='mg':
            print(f"{a*1000000} mgs")
        elif To=='g':
            print(f"{a*1000} grams")
        elif To=='ton':
            print(f"{a*0.001} Tons")
        elif To=='stone':
            print(f"{a*0.157473} Stones")
        elif To=='pounds':
            print(f"{a*2.20462} Pounds")
        else:
            print("Enter a valid unit!!")
    if From=='mg':
        if To=='kg':
            print(f"{a*0.0000001} kgs")
        elif To=='mg':
            print(f"{a} mgs")
        elif To=='g':
            print(f"{a*0.001} grams")
        elif To=='ton':
            print(f"{a*0.0000000010231} Tons")
        elif To=='stone':
            print(f"{a*0.000000157473} Stones")
        elif To=='pounds':
            print(f"{a*0.00000220462} Pounds")
        else:
            print("Enter a valid unit!!")
    if From=='g':
        if To=='kg':
            print(f"{a*0.001} kgs")
        elif To=='mg':
            print(f"{a*1000} mgs")
        elif To=='g':
            print(f"{a} grams")
        elif To=='ton':
            print(f"{a*0.00000110231} Tons")
        elif To=='stone':
            print(f"{a*0.000157473} Stones")
        elif To=='pounds':
            print(f"{a*0.00220462} Pounds")
        else:
            print("Enter a valid unit!!")
    if From=='ton':
        if To=='kg':
            print(f"{a*907.185} kgs")
        elif To=='mg':
            print(f"{a*907185000} mgs")
        elif To=='g':
            print(f"{a*907185} grams")
        elif To=='ton':
            print(f"{a} Tons")
        elif To=='stone':
            print(f"{a*142.857} Stones")
        elif To=='pounds':
            print(f"{a*2000} Pounds")
        else:
            print("Enter a valid unit!!")
    if From=='stone':
        if To=='kg':
            print(f"{a*6.35029} kgs")
        elif To=='mg':
            print(f"{a*6350290} mgs")
        elif To=='g':
            print(f"{a*6350.29} grams")
        elif To=='ton':
            print(f"{a*0.007} Tons")
        elif To=='stone':
            print(f"{a} Stones")
        elif To=='pounds':
            print(f"{a*14} Pounds")
        else:
            print("Enter a valid unit!!")
    if From=='pounds':
        if To=='kg':
            print(f"{a*0.453592} kgs")
        elif To=='mg':
            print(f"{a*453592} mgs")
        elif To=='g':
            print(f"{a*453.592} grams")
        elif To=='ton':
            print(f"{a*0.0005} Tons")
        elif To=='stone':
            print(f"{a*0.0714286} Stones")
        elif To=='pounds':
            print(f"{a} Pounds")
        else:
            print("Enter a valid unit!!")
    h=(input("Do you want to continue(Y/N):"))
    if h=='Y':
        i=0
    else:
        print("closing the weight calculator...")
        break
