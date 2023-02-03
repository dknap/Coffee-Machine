from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_machine = MoneyMachine()

is_on = True
while is_on:
    items = my_menu.get_items()[:-1]
    choice = input(f"What would you like? {items}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffee_maker.report()
        my_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        if drink:
            if my_coffee_maker.is_resource_sufficient(drink) and my_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)