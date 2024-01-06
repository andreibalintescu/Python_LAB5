from Modelle.DISHES.FOOD_DRINK import *
from Modelle.IDS.ID import *
from Modelle.CUSTOMERS_AND_ORDERS.CUSTOMERS_ORDERS import *

class Console:
    def __init__(self,controller):
        self.controller = controller

    def menu(self):
        return """
        1 - Gerichten
        2 - Kunden
        3 - Bestellungen
        0 - Exit
        """

    def foodmenu(self):
        return """
        1 - Gericht hinzufügen
        2 - GekochtesGericht hinzufügen
        3 - Getränk hinzufügen
        4 - Alle speichern
        5 - Neu laden
        0 - Abbrechen
        """

    def customermenu(self):
        return """
        1 - Kunde hinzufügen
        2 - Kunde suchen
        0 - Abbrechen
        """

    def ordermenu(self):
        return """
        
        """
    def run(self):
        while True:
            print(self.menu())
            dishes = []
            drinks = []
            customers = []
            orders = []
            value = int(input())
            if value == 0:
                break
            if value == 1:
                while True:
                    print(self.foodmenu())
                    food_value = int(input())
                    if food_value == 1:
                        id = input("Id von Gericht:")
                        name = input("Name von Gericht:")
                        portion_size = input("Portionsgröße:")
                        price = input("Preis:")
                        dish = Dish(id, name, portion_size, price)
                        dishes.append(dish)

                    if food_value == 2:
                        id = input("Id von Gericht:")
                        name = input("Name von gekochtes Gericht:")
                        portion_size = input("Portionsgröße:")
                        price = input("Preis:")
                        cooking_time = input("Zubereitungszeit:")
                        cooked_dish = CookedDish(id, name, portion_size, price, cooking_time)
                        dishes.append(cooked_dish)

                    if food_value == 3:
                        id = input("Id von Getränk:")
                        name = input("Name von Getränk:")
                        portion_size = input("Portionsgröße:")
                        price = input("Preis:")
                        alcohol_percentage = input("Alkoholgehalt:")
                        drink = Drink(id, name, portion_size, price, alcohol_percentage)
                        drinks.append(drink)

                    if food_value == 4:
                        self.controller.add_dishes(dishes)
                        list_of_dishes = self.controller.load_dishes()
                        text = self.controller.convert_string_dish(list_of_dishes)
                        self.controller.write_dishes(str(text))
                        dishes.clear()

                        self.controller.add_drinks(drinks)
                        list_of_drinks = self.controller.load_drinks()
                        text = self.controller.convert_string_drink(list_of_drinks)
                        self.controller.write_drinks(str(text))
                        drinks.clear()

                    if food_value == 5:
                        string_drinks = self.controller.read_drinks()
                        string_dishes = self.controller.read_dishes()
                        open('Dish_Data', 'w').close()
                        open('Drink_Data', 'w').close()
                        if string_drinks != '':
                            list_of_drinks = self.controller.convert_from_string_drink(string_drinks)
                            drinks.extend(list_of_drinks)
                        if string_dishes != '':
                            list_of_dishes = self.controller.convert_from_string_dish(string_dishes)
                            dishes.extend(list_of_dishes)

                    if food_value == 0:
                        break

            if value == 2:
                while True:
                    print(self.customermenu())
                    customer_value = int(input())
                    if customer_value == 1:
                        id = input("Id von Kunde:")
                        name = input("Name und Vorname des Kundes:")
                        address = input("Adresse:")
                        customer = Customer(id, name, address)
                        customers.append(customer)

            if value == 3:
                while True:
                    print(self.ordermenu())
                    order_value = int(input())







