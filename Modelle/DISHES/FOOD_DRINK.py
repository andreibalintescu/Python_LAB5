from Modelle.IDS.ID import Identifiable
class Dish(Identifiable):     #Erbt von Identifizierbar. Es erbt die Attribute und Methoden von der ObereKlasse.
    def __init__(self, id, name, portion_size, price):
        Identifiable.__init__(self, id)
        self.name = name
        self.portion_size = portion_size
        self.price = price


class CookedDish(Dish):  #Erbt von Gericht. Es ist eine UntereKlasse von Gericht.
    def __init__(self, id, name, portion_size, price, cooking_time):
        Dish.__init__(self, id, name, portion_size, price)
        self.cooking_time = cooking_time

class Drink(Dish):   #Erbt von Gericht. Es ist eine UntereKlasse von Gericht.
    def __init__(self, id, name, portion_size, price, alcohol_percentage):
        Dish.__init__(self, id, name, portion_size, price)
        self.alcohol_percentage = alcohol_percentage

#Beide Klassen erben die Attribute von der ObereKlasse Gericht, z.B. Id, Name, PortionGroße und Alkoholgehalt.