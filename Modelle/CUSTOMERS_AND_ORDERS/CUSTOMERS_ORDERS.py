from Modelle.IDS.ID import Identifiable
import functools
class Customer(Identifiable):
    def __init__(self, id, name, address):
        Identifiable.__init__(self,id)
        self.name = name
        self.address = address

class Order(Identifiable):
    def __init__(self, id, customer_id, dishes_id_list, drinks_id_list, total_price):
        Identifiable.__init__(self, id)
        self.customer_id = customer_id
        self.dishes_id_list = dishes_id_list
        self.drinks_id_list = drinks_id_list
        self.total_price = total_price

    def calculate_total_price(self):
        pass
    def __generate_invoice(self):
        pass
    def print_invoice(self):
        pass