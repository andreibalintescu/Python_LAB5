from Modelle.IDS.ID import Identifiable
class Dish(Identifiable):
    def __init__(self,id,weight,price):
        Identifiable.__init__(self,id)
        self.weight = weight
        self.price = price

class Cooked_Dish(Dish):
    def __init__(self,id,weight,price,cooking_time):
        Dish.__init__(self,id,weight,price)
        self.cooking_time = cooking_time

class Beverage(Dish):
    def __init__(self,id,weight,price,alcohol_percentage):
        Dish.__init__(self,id,weight,price)
        self.alcohol_percentage = alcohol_percentage
