import ast
import pickle
from Modelle.DISHES.FOOD_DRINK import *
from Modelle.CUSTOMERS_AND_ORDERS.CUSTOMERS_ORDERS import Customer, Order


class DataRepo:
    def __init__(self, file):
        self.file = file

    def save(self, data):
        with open(self.file, 'ab') as f:
            pickle.dump(data, f)

    def load(self):
        with open(self.file, 'rb') as f:
            return pickle.load(f)

    def read_file(self):
        with open(self.file, "r") as f:
            return f.read()

    def write_to_file(self, data):
        with open(self.file, "w") as file:
            file.write(data)

    def convert_to_string(self):
        pass

    def convert_from_string(self):
        pass


class CookedDishRepo(DataRepo):
    def convert_to_string(self, list_of_dishes):
        def pack_stats(dish):

            stats = []
            if type(dish) == Dish:
                stats.append(dish.id)
                stats.append(dish.name)
                stats.append(dish.portion_size)
                stats.append(dish.price)
            else:
                stats.append(dish.id)
                stats.append(dish.name)
                stats.append(dish.portion_size)
                stats.append(dish.price)
                stats.append(dish.cooking_time)
            return tuple(stats)

        text = list(map(pack_stats, list_of_dishes))
        return text

    def convert_from_string(self, stringy):
        def unpack_stats(stats):
            if len(stats) == 4:
                id, name, portion_size, price = stats
                dish = Dish(id, name, portion_size, price)
                return dish
            if len(stats) == 5:
                id, name, portion_size, price, cooking_time = stats
                cooked_dish = CookedDish(id, name, portion_size, price, cooking_time)
                return cooked_dish

        list_of_tuples = list(ast.literal_eval(stringy))
        list_of_dishes = list(map(unpack_stats, list_of_tuples))
        return list_of_dishes


class DrinkRepo(DataRepo):
    def convert_to_string(self, list_of_drinks):
        def pack_stats(drink):
            stats = []
            stats.append(drink.id)
            stats.append(drink.name)
            stats.append(drink.portion_size)
            stats.append(drink.price)
            stats.append(drink.alcohol_percentage)
            return tuple(stats)

        text = list(map(pack_stats, list_of_drinks))
        return text

    def convert_from_string(self, stringy):
        def unpack_stats(stats):
            id, name, portion_size, price, alcohol_percentage = stats
            drink = Drink(id, name, portion_size, price, alcohol_percentage)
            return drink

        list_of_tuples = list(ast.literal_eval(stringy))
        list_of_drinks = list(map(unpack_stats, list_of_tuples))
        return list_of_drinks


class CustomerRepo(DataRepo):
    def convert_to_string(self, list_of_customers):
        def pack_stats(customer):
            stats = []
            stats.append(customer.id)
            stats.append(customer.name)
            stats.append(customer.address)
            return tuple(stats)

        text = list(map(pack_stats, list_of_customers))
        return text

    def convert_from_string(self, stringy):
        def unpack_stats(stats):
            id, name, address = stats
            customer = Customer(id, name, address)
            return customer

        list_of_tuples = list(ast.literal_eval(stringy))
        list_of_customers = list(map(unpack_stats, list_of_tuples))
        return list_of_customers


class OrderRepo(DataRepo):
    def convert_to_string(self, list_of_orders):
        def pack_stats(order):
            stats = []
            stats.append(order.id)
            stats.append(order.customer_id)
            stats.append(order.dishes_id_list)
            stats.append(order.drinks_id_list)
            stats.append(order.total_price)
            return tuple(stats)

        text = list(map(pack_stats, list_of_orders))
        return text

    def convert_from_string(self, stringy):
        def unpack_stats(stats):
            id, customer_id, dishes_id_list, drinks_id_list, total_price = stats
            order = Order(id, customer_id, dishes_id_list, drinks_id_list, total_price)
            return order

        list_of_tuples = list(ast.literal_eval(stringy))
        list_of_orders = list(map(unpack_stats, list_of_tuples))
        return list_of_orders
