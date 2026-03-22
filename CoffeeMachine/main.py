from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()
on = True

while on:
    # Ask user what they want
    drink = input(f"{menu.get_items()}. " + "What would you like? ")
    # Turn off the Coffee Machine by entering "off" to the prompt
    if drink == "off":
        on = False
    elif drink == "report":
      # Print report
        print(machine.report())
        print(money.report())
    else:
      order = menu.find_drink(drink)
      # Check if resources sufficient
      machine.is_resource_sufficient(order)
      print(f"That will be ${order.cost}.")
      # Process coins
      if money.make_payment(order.cost):
         # Make coffee
         machine.make_coffee(order)
