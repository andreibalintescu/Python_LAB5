from Controller.Controller import *
from Repository.DATA.DATA_REPOS import *
from UI.Console import *


def main():
    console = Console(
        RestaurantController(CookedDishRepo('Dish_Data'), DrinkRepo('Drink_Data'), CustomerRepo('Customers_Data'),
                             OrderRepo('Orders_Data')))
    console.run()


main()
