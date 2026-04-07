# Concession Stand PRogram
cart=[]
total=0
menu={'Cheese Popcorn': 10,
      'Butter Popcorn': 7,
      'Normal Popcorn': 5,
      'Nachos': 15,
      'Extra dip':2,
      'sandwhich':12,
      'Pepsi':10,
      'Coke':10,}
print("---------------Menu---------------")
for key,value in menu.items():
    print(f"{key:20}:${value:05,.2f}")
while True:
    key=input("Enter the item you want to buy (Q to Quit):")
    if key.upper()=='Q':
        break
    else:
        cart.append(key)
        total+=menu.get(key)
print("==========Your Cart==========")
for x in cart:
    print(x)
print(f"Your total bill is ${total:.2f}")
