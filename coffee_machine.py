MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# The initial resources available in the machine
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredient):
    """Return True when order can be made, False if ingredients are insufficient."""
    for  item in order_ingredient: 
        if order_ingredient[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    """Returns the total calculated from coins inserted."""
    print("please insert coins.")
    total = int(input("How Many quarter?: ")) * 0.25
    total += int(input("How Many dimes?: ")  ) * 0.01
    total += int(input("How Many nickles?: ")) * 0.05
    total += int(input("How Many panies?: ") ) * 0.01
    return total

def is_transaction_succcessful(money_recieved, drink_cost):
    """Return True when the payment is accepted, or False if the money is insufficient."""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry thats not enoough money. Money refuned")
        return False
    
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice ==  "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            is_transaction_succcessful(payment, drink["cost"]) 
