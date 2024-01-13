from Modelle.DISHES.FOOD_DRINK import *
from Modelle.CUSTOMERS_AND_ORDERS.CUSTOMERS_ORDERS import *


# Benutzeroberfläche für der Anwendung.
class Console:
    def __init__(self, controller):
        self.controller = controller

    def main_menu(self):
        return """
        1 - Gerichten
        2 - Kunden
        3 - Bestellungen
        0 - Exit
        """

    def food_menu(self):
        return """
        1 - Gerichten anzeigen
        2 - Gerichten hinzufügen
        3 - Gerichten aktualisieren
        4 - Gerichten löschen
        5 - Alle Änderungen speichern
        6 - Neu laden
        0 - Abbrechen
        """

    def food_add_menu(self):
        return """
        1 - Gericht hinzufügen
        2 - Gekochtes Gericht hinzufügen
        3 - Getränk hinzufügen
        0 - Fertig
        """

    def food_change_menu(self):
        return """
        1 - Gericht aktualisieren
        2 - Gekochtes Gericht aktualisieren
        3 - Getränk aktualisieren
        0 - Fertig
        """

    def food_erase_menu(self):
        return """
        1 - Gericht löschen
        2 - Gekochtes Gericht löschen
        3 - Getränk löschen
        0 - Fertig
        """

    def customermenu(self):
        return """
        1 - Kunden anzeigen
        2 - Kunde suchen
        3 - Kunde hinzufügen
        4 - Kunde aktualisieren
        5 - Kunde löschen
        6 - Alle Änderungen speichern
        7 - Neu laden
        0 - Abbrechen
        """

    def ordermenu(self):
        return """
        1 - Bestellungen anzeigen
        2 - Bestellung hinzufügen
        3 - Bestellung löschen
        4 - Alle Änderungen speichern
        5 - Neu laden
        0 - Abbrechen
        """

    def run(self):
        while True:
            print(self.main_menu())
            dishes = []
            drinks = []
            customers = []
            orders = []
            value = int(input())
            if value == 0:
                break
            if value == 1:
                while True:
                    print(self.food_menu())
                    food_value = int(input())
                    if food_value == 1:  # Dataien Inhalt lesen
                        with open('Dish_Data', 'r') as f:
                            print(f.read())
                        with open('Drink_Data', 'r') as f:
                            print(f.read())
                    if food_value == 2:  # Neue Objekte erstellen und Hinzufügen
                        while True:
                            print(self.food_add_menu())
                            add_food_value = int(input())
                            if add_food_value == 1:
                                id = input("Id von Gericht:")
                                name = input("Name von Gericht:")
                                portion_size = input("Portionsgröße:")
                                price = input("Preis:")
                                dish = Dish(id, name, portion_size, price)
                                dishes.append(dish)
                            if add_food_value == 2:
                                id = input("Id von Gericht:")
                                name = input("Name von gekochtes Gericht:")
                                portion_size = input("Portionsgröße:")
                                price = input("Preis:")
                                cooking_time = input("Zubereitungszeit:")
                                cooked_dish = CookedDish(id, name, portion_size, price, cooking_time)
                                dishes.append(cooked_dish)
                            if add_food_value == 3:
                                id = input("Id von Getränk:")
                                name = input("Name von Getränk:")
                                portion_size = input("Portionsgröße:")
                                price = input("Preis:")
                                alcohol_percentage = input("Alkoholgehalt:")
                                drink = Drink(id, name, portion_size, price, alcohol_percentage)
                                drinks.append(drink)
                            if add_food_value == 0:
                                break

                    if food_value == 3:  # Objekte aktualisieren
                        while True:
                            print(self.food_change_menu())
                            change_food_value = int(input())
                            if change_food_value == 1:
                                id = input("Id von Gericht, die Sie aktualisieren möchten:")
                                for i in range(0, len(dishes)):
                                    if dishes[i].id == id:
                                        dishes[i].name = input("Name von Gericht:")
                                        dishes[i].portion_size = input("Portionsgröße:")
                                        dishes[i].price = input("Preis:")

                            if change_food_value == 2:
                                id = input("Id von  Gekochtes Gericht, die Sie aktualisieren möchten:")
                                for i in range(0, len(dishes)):
                                    if dishes[i].id == id:
                                        dishes[i].name = input("Name von Gekochtes Gericht:")
                                        dishes[i].portion_size = input("Portionsgröße:")
                                        dishes[i].price = input("Preis:")
                                        dishes[i].cooking_time = input("Zubereitungszeit:")

                            if change_food_value == 3:
                                id = input("Id von  Getränk, die Sie aktualisieren möchten:")
                                for i in range(0, len(drinks)):
                                    if drinks[i].id == id:
                                        drinks[i].name = input("Name von Getränk:")
                                        drinks[i].portion_size = input("Portionsgröße:")
                                        drinks[i].price = input("Preis:")
                                        drinks[i].alcohol_percentage = input("Alkoholgehalt:")
                            if change_food_value == 0:
                                break

                    if food_value == 4:  # Objekte löschen
                        while True:
                            print(self.food_erase_menu())
                            erase_food_value = int(input())
                            if erase_food_value == 1:
                                id = input("Id von Gericht, die Sie löschen möchten:")

                                def fun(dish):
                                    if dish.id != id:
                                        return True
                                    else:
                                        return False

                                dishes = list(filter(fun, dishes))

                            if erase_food_value == 2:
                                id = input("Id von Gekochtes Gericht, die Sie löschen möchten:")

                                def fun(dish):
                                    if dish.id != id:
                                        return True
                                    else:
                                        return False

                                dishes = list(filter(fun, dishes))
                            if erase_food_value == 3:
                                id = input("Id von  Getränk, die Sie löschen möchten:")

                                def fun(drink):
                                    if drink.id != id:
                                        return True
                                    else:
                                        return False

                                drinks = list(filter(fun, drinks))

                            if erase_food_value == 0:
                                break

                    if food_value == 5:  # Alle speichern
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

                    if food_value == 6:  # Neu laden
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
                        with open('Customers_Data', 'r') as f:
                            print(f.read())
                    if customer_value == 2:
                        search = input("Such Kunde nach Name oder Adresse:")
                        customer_info = self.controller.search_customers(customers, search)
                        print(customer_info)
                    if customer_value == 3:
                        id = input("Id von Kunde:")
                        name = input("Name und Vorname des Kunden:")
                        address = input("Adresse:")
                        customer = Customer(id, name, address)
                        customers.append(customer)

                    if customer_value == 4:
                        id = input("Id von Kunde, die Sie aktualisieren möchten:")
                        for i in range(0, len(customers)):
                            if customers[i].id == id:
                                customers[i].name = input("Name von Kunde:")
                                customers[i].address = input("Adresse:")

                    if customer_value == 5:
                        id = input("Id von Kunde, die Sie löschen möchten:")

                        def fun(customer):
                            if customer.id != id:
                                return True
                            else:
                                return False

                        customers = list(filter(fun, customers))

                    if customer_value == 6:
                        self.controller.add_customers(customers)
                        list_of_customers = self.controller.load_customers()
                        text = self.controller.convert_string_customer(list_of_customers)
                        self.controller.write_customers(str(text))
                        customers.clear()

                    if customer_value == 7:
                        string_customers = self.controller.read_customers()
                        open('Customers_Data', 'w').close()
                        if string_customers != '':
                            list_of_customers = self.controller.convert_from_string_customer(string_customers)
                            customers.extend(list_of_customers)
                    if customer_value == 0:
                        break

            if value == 3:
                while True:
                    print(self.ordermenu())
                    order_value = int(input())
                    if order_value == 1:
                        id_from_customer = input("Geben Sie die ID von Kunde ein, um seine Bestellung herauszufinden:")
                        given_order = self.controller.find_order(orders, id_from_customer)
                        invoice = given_order.call_generate_invoice(dishes, drinks)
                        given_order.print_invoice(invoice)

                    if order_value == 2:
                        id = input("Id von Bestellung:")
                        customer_id = input("Id von Kunde:")
                        dishes_id_list = input("Ids von bestellten Gerichten:")
                        drinks_id_list = input("Ids von bestellten Getränke:")
                        total_price = 0
                        order = Order(id, customer_id, dishes_id_list, drinks_id_list, total_price)
                        orders.append(order)
                        list_of_ids = list(dishes_id_list.strip().split(",")) + list(drinks_id_list.strip().split(","))

                        def get_prices(list_of_ids):
                            prices = []
                            for drink in drinks:
                                if drink.id in list_of_ids:
                                    prices.append(int(drink.price))
                            for dish in dishes:
                                if dish.id in list_of_ids:
                                    prices.append(int(dish.price))
                            return prices

                        list_of_prices = get_prices(list_of_ids)
                        order.calculate_total_price(list_of_prices)
                    if order_value == 3:
                        id = input("Id von Bestellung, die Sie löschen möchten:")

                        def fun(order):
                            if order.id != id:
                                return True
                            else:
                                return False

                        orders = list(filter(fun, orders))

                    if order_value == 4:
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

                        self.controller.add_customers(customers)
                        list_of_customers = self.controller.load_customers()
                        text = self.controller.convert_string_customer(list_of_customers)
                        self.controller.write_customers(str(text))
                        customers.clear()

                        self.controller.add_orders(orders)
                        list_of_orders = self.controller.load_orders()
                        text = self.controller.convert_string_order(list_of_orders)
                        self.controller.write_orders(str(text))
                        orders.clear()

                    if order_value == 5:
                        string_drinks = self.controller.read_drinks()
                        string_dishes = self.controller.read_dishes()
                        string_customers = self.controller.read_customers()
                        string_orders = self.controller.read_orders()
                        open('Dish_Data', 'w').close()
                        open('Drink_Data', 'w').close()
                        open('Customers_Data', 'w').close()
                        open('Orders_Data', 'w').close()
                        if string_drinks != '':
                            list_of_drinks = self.controller.convert_from_string_drink(string_drinks)
                            drinks.extend(list_of_drinks)
                        if string_dishes != '':
                            list_of_dishes = self.controller.convert_from_string_dish(string_dishes)
                            dishes.extend(list_of_dishes)
                        if string_customers != '':
                            list_of_customers = self.controller.convert_from_string_customer(string_customers)
                            customers.extend(list_of_customers)
                        if string_orders != '':
                            list_of_orders = self.controller.convert_from_string_order(string_orders)
                            orders.extend(list_of_orders)

                    if order_value == 0:
                        break
