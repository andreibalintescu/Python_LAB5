#Der RestaurantController koordiniert die Interaktion zwischen den Repositories und der Benutzeroberfläche.

class RestaurantController:
    def __init__(self, dish_repo, drink_repo, customer_repo, order_repo):
        self.dish_repo = dish_repo
        self.drink_repo = drink_repo
        self.customer_repo = customer_repo
        self.order_repo = order_repo

    def add_drinks(self, drinks):
        self.drink_repo.save(drinks)

    def load_drinks(self):
        return self.drink_repo.load()

    def read_drinks(self):
        return self.drink_repo.read_file()

    def convert_string_drink(self, list_of_drinks):
        return self.drink_repo.convert_to_string(list_of_drinks)

    def convert_from_string_drink(self, string_of_drinks):
        return self.drink_repo.convert_from_string(string_of_drinks)

    def write_drinks(self, content):
        self.drink_repo.write_to_file(content)
#/////////////////////////////////////////////////
    def add_dishes(self, dishes):
        self.dish_repo.save(dishes)

    def load_dishes(self):
        return self.dish_repo.load()

    def read_dishes(self):
        return self.dish_repo.read_file()

    def convert_string_dish(self, list_of_dishes):
        return self.dish_repo.convert_to_string(list_of_dishes)

    def convert_from_string_dish(self, string_of_dishes):
        return self.dish_repo.convert_from_string(string_of_dishes)

    def write_dishes(self, content):
        self.dish_repo.write_to_file(content)
#////////////////////////////////////////////////////////////
    def add_customers(self,customer):
        self.customer_repo.save(customer)

    def load_customers(self):
        return self.customer_repo.load()

    def search_customers(self, customers, search):
        string = ""
        def fun(customer):
            if (search in customer.name.lower() or search in customer.address.lower()) or (search in customer.name.upper() or search in customer.address.upper()):
                return True
            else:
                return False

        searched_customers = list(filter(fun, customers))
        for customer in searched_customers:
            string = string + " " + customer.id + " " + customer.name + " " + customer.address + "\n"

        return string

    def read_customers(self):
        return self.customer_repo.read_file()

    def convert_string_customer(self, list_of_customers):
        return self.customer_repo.convert_to_string(list_of_customers)

    def convert_from_string_customer(self, string_of_customers):
        return self.customer_repo.convert_from_string(string_of_customers)

    def write_customers(self, content):
        self.customer_repo.write_to_file(content)
#//////////////////////////////////////////////////////////////////
    def add_orders(self,order):
        self.order_repo.save(order)

    def load_orders(self):
        return self.order_repo.load()
    def find_order(self, orders, customer_id):
        for order in orders:
            if customer_id == order.customer_id:
                return order

    def read_orders(self):
        return self.order_repo.read_file()

    def convert_string_order(self, list_of_orders):
        return self.order_repo.convert_to_string(list_of_orders)

    def convert_from_string_order(self, string_of_orders):
        return self.order_repo.convert_from_string(string_of_orders)

    def write_orders(self, content):
        self.order_repo.write_to_file(content)


