
print("====shopping list ====")


options = ("pls enter items into your cart and if done entering item input 'Exit'")
print (options)
cart = []

        
def enter_item():
    while True:
        your_item  = input("enter the item: ").capitalize()
        if your_item != "Exit":
            cart.append(your_item)
        if your_item == "Exit":
            for item in cart:
                print(item)
            break
enter_item()
