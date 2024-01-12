from Modelle.IDS.ID import Identifiable
import functools
class Customer(Identifiable):
    def __init__(self, id, name, address):
        Identifiable.__init__(self, id)
        self.name = name
        self.address = address

class Order(Identifiable):
    def __init__(self, id, customer_id, dishes_id_list, drinks_id_list, total_price):
        Identifiable.__init__(self, id)
        self.customer_id = customer_id
        self.dishes_id_list = dishes_id_list
        self.drinks_id_list = drinks_id_list
        self.total_price = total_price

    def calculate_total_price(self, list_of_prices):
        self.total_price = functools.reduce(lambda a, b: a+b, list_of_prices)

    def __generate_invoice(self, dishes, drinks):
        invoice = ""
        invoice = invoice + "Hier ist Ihre Bestellung:" + "\n"
        for dish in dishes:
            if dish.id in self.dishes_id_list:
                invoice = invoice + f"{dish.name}..................................{dish.price}" + "\n"
        for drink in drinks:
            if drink.id in self.drinks_id_list:
                invoice = invoice + f"{drink.name}.................................{drink.price}" + "\n"
        invoice = invoice + f"Ihre Gesamtkosten für die Bestellung ist {self.total_price} Euro" + "\n"
        invoice = invoice + "Vielen Dank und wir warten auf Sie!" + "\n"
        return invoice

    def call_generate_invoice(self, dishes, drinks): #Offentliche Methode zum Aufrufen einer privaten Methode.
        return self.__generate_invoice(dishes, drinks)

    def print_invoice(self, invoice):
        print(invoice)

#Beide Klassen erben von Identifizierbar,
# aber die Bestellung Klasse hat einzige Methoden für Generierung des Rechnungs und Berechnung des Gesamtkostes.