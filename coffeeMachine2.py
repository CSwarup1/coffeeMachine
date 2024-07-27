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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_sufficient(drink_ingredients, resources):
    is_ok=True
    for items in drink_ingredients:
        if drink_ingredients[items] > resources [items]:
            print (f"Sorry there is no sufficient {items}")
            is_ok=False
    return  is_ok

def process_coins():
    print("enter the coins\n")
    total=int(input("Enter the no. of quarters "))*0.25
    total+=int(input("enter the no. of dimes "))*0.10
    total+=int(input("Enter the no. of nickles "))*0.05
    total+=int(input("enter the no. of pennies "))*0.01
    return(total)


def transaction_successful(pay, costOfDrink):
    if pay>=costOfDrink:
        change=pay-costOfDrink
        print (f"here's ur change: ${change}")
        global profit
        profit+=costOfDrink
        return True
    
def process_coffee(drink, ingredients_needed):
    print(drink)
    for items in ingredients_needed:
        resources[items]-=ingredients_needed[items]
    print(f"here's ur {drink}")


to_do=True
while to_do:
    user=input("What would you like (espresso/ latte / cappuccino)  or u  can ask for 'report'or can say 'end' the process ")
    if user=='end':
        to_do=False
        print("thankyou")
    elif user=='report':
        print(f"water: {resources['water']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"milk: {resources['milk']}ml")
        print(f"money: ${'profit'}")
    else:
        drink=MENU[user]
        if resources_sufficient(drink['ingredients'],resources):
            payment=process_coins()
            if transaction_successful(payment, drink['cost']):
                process_coffee(user,drink['ingredients'])
        
        

        


  
    
    