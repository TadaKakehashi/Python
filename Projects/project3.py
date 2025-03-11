menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'coffee':80,
    'salad':100,
}

print("Welcome to our restaurant!")
print("Pizza : Rs40\nPasta : Rs50\nBurger : Rs60\nCoffee : Rs80\nSalad : Rs100")

order_total = 0

item_1 = input("Enter the name of item you want to order = ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f'Your item {item_1} has been added to your order')
else:
    print("Sorry we don't have that item")

another_order = input("Would you like to order another item? ").lower()
if another_order == "yes":
    item_2 = input("Enter the name of item you want to order = ")
    order_total += menu[item_2]
    print(f'Your order {item_2} has been added to your order')
elif another_order == "no":
    print(f'Your order total is {order_total}')
else:
    print("Sorry we don't have that item")

