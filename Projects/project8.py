coffee_resource = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
}

cost_coffee = {
    "espresso": 12.99,
    "latte": 9.99,
    "cappuccino": 15.99
}

recipes = {
    "espresso": {"Water": 80, "Coffee": 20},
    "latte": {"Water": 150, "Milk": 50, "Coffee": 24},
    "cappuccino": {"Water": 250, "Milk": 100, "Coffee": 24}
}

profit = 0.0


def is_resource_sufficient(recipe):
    for item in recipe:
        if recipe[item] > coffee_resource.get(item, 0):
            print(f"Sorry, not enough {item}.")
            return False
    return True


def process_transaction(user_money, cost):
    if user_money >= cost:
        change = round(user_money - cost, 2)
        if change > 0:
            print(f"Here is Rs {change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        break

    elif user_input == "report":
        for key, value in coffee_resource.items():
            unit = "g" if key == "Coffee" else "ml"
            print(f"{key} : {value}{unit}")
        print(f"Money : Rs {profit}")

    elif user_input in recipes:
        recipe = recipes[user_input]
        if is_resource_sufficient(recipe):
            user_money = float(input(f"Please insert money (Cost: Rs {cost_coffee[user_input]}): "))
            if process_transaction(user_money, cost_coffee[user_input]):
                for item in recipe:
                    coffee_resource[item] -= recipe[item]
                print(f"Here is your {user_input}. Enjoy!")

    else:
        print("Invalid input. Please try again.")
