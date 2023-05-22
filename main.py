from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True

while machine_is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/):")

    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        coffee_machine.report()
