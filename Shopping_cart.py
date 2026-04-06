#shopping cart program
try:
    foods=[]
    prices=[]
    total=0
    print("Welcome to FalBazaar🥳🙏...")
    print("Add your products into the cart and enter q for quitting.")
    while True:
        cart=str(input("Enter the food item you want to add to cart:"))
        if (cart.lower()=='q'):
            print("checking out....")
            break
        else:
            price=float(input("Enter the price in $ of the item:"))
            total+=price
            foods.append(cart)
    if len(foods)==0:
        print("Your cart is empty!!")
    else:
        print("-------Your Cart-------")
        print(foods)
    print(f"Your Total is ${total:.2f} \n Please visit our store again🤗!!")
except Exception as e:
    print(e)
    print("Enter the inputs correctly -_- ")
