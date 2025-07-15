
class Machine:

    def __init__(self, water, milk, coffee, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

    def __str__(self):
        ret_str = f"\nMachine Resources:\nWater: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: ${self.money}\n"
        return ret_str
    
class Drink:

    def __init__(self, water, milk, coffee, cost):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost

    def __str__(self):
        ret_str = f"Recipe is:\nWater: {self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nCost: ${self.cost}\n"
        return ret_str


    
# Function for printing report of what the coffee is left with and money


# Function for checking if the machine has enough resources left
def check_resources(drink, machine):

    check_water = (machine.water - drink.water) >= 0
    check_milk = (machine.milk - drink.milk) >= 0
    check_coffee = (machine.coffee - drink.coffee) >= 0
    
    if check_water and check_milk and check_coffee:
        return True
    else:
        return False
    
def make_drink(drink, machine):
    machine.water = machine.water - drink.water
    machine.milk = machine.milk - drink.milk
    machine.coffee = machine.coffee - drink.coffee
    machine.money = machine.money + drink.cost

    return machine
    
def print_menu():

    menu_str = "1. Make a coffee\n2. View Machine Report\n3. Turn Off\n"

    return menu_str

# Main coffee function
def coffee():

    machine_on = True

    coffee_machine = Machine(300, 200, 100, 0)

    espresso = Drink(50, 0, 18, 1.5)

    latte = Drink(200, 150, 24, 2.5)

    cappucino = Drink(250, 100, 24, 3)

    while machine_on:

        print(print_menu())

        coffee_dict = {"espresso": espresso, "cappucino": cappucino, "latte": latte}

        choice = int(input("Please pick an option (1, 2, 3): "))

        if choice == 1:

            type = input("What would you like? (espresso/latte/cappucino): ")
            drink = coffee_dict[type]

            enough_resources = check_resources(drink, coffee_machine)
            print(enough_resources)
            if enough_resources:
                coffee_machine = make_drink(drink, coffee_machine)
                print(f"Here is your {type}.\n")
            else:
                print("Not enough resouces in machine. Please refill.")
        elif choice == 2:
            print(coffee_machine)
        else:
            machine_on = False 
    

coffee()


