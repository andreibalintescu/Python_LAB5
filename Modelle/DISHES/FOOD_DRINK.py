from Modelle.IDS.ID import Identifiable
class Dish(Identifiable):
    def __init__(self, id, name, portion_size, price):
        Identifiable.__init__(self, id)
        self.name = name
        self.portion_size = portion_size
        self.price = price


class CookedDish(Dish):
    def __init__(self, id, name, portion_size, price, cooking_time):
        Dish.__init__(self, id, name, portion_size, price)
        self.cooking_time = cooking_time

class Drink(Dish):
    def __init__(self, id, name, portion_size, price, alcohol_percentage):
        Dish.__init__(self, id, name, portion_size, price)
        self.alcohol_percentage = alcohol_percentage

