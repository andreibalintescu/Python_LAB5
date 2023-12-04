from Modelle.IDS.ID import Identifiable
from Modelle.DISHES.FOOD_BEVERAGE import *
from Modelle.CUSTOMERS_AND_ORDERS.CUSTOMERS_ORDERS import *
from Repository.DATA.DATA_REPOS import *

drink_repo = DrinkRepo('Drinks_Data')

drink1 = Beverage('Vodka', "300ml", 50, 80)
drink2 = Beverage('Water', "1L", 14.5, 0)
drinks1 = [drink1, drink2]
stringy = drink_repo.convert_to_string(drinks1)
drink_repo.save('Drinks_Data', stringy)
string = drink_repo.load('Drinks_Data')




