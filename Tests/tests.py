import unittest
from Controller.Controller import *
from Repository.DATA.DATA_REPOS import *
from Modelle.DISHES.FOOD_DRINK import *

class TestAddDish(unittest.TestCase):
    def setUp(self):
        self.controller = RestaurantController(CookedDishRepo('test_Dish_Data'), None, None, None)

    def test_add_cooked_dish(self):
        test_cooked_dish = CookedDish("1", "Goulash","450g", "14", "30 Minutes")

        self.controller.add_dishes([test_cooked_dish])

        loaded_dishes = self.controller.load_dishes()

        for item in loaded_dishes:
            if item.id == test_cooked_dish.id and item.name == test_cooked_dish.name and item.portion_size == test_cooked_dish.portion_size and item.price == test_cooked_dish.price and item.cooking_time == test_cooked_dish.cooking_time:
                return True

    def tearDown(self):
        # Clean up by removing the test file
        open('test_Dish_Data', 'w').close()


test1 = TestAddDish()
test1.setUp()
test1.test_add_cooked_dish()
test1.tearDown()
class TestSearchCustomers(unittest.TestCase):
    def setUp(self):

        self.controller = RestaurantController(None, None, CustomerRepo('test_Customers_Data'), None)

    def test_search_customers(self):
        # Create test customers
        customer1 = Customer("1", 'Bob', 'Sesame Street nr. 4')
        customer2 = Customer('2', 'Bobinson', 'Wolf Street nr. 65')

        self.controller.add_customers([customer1, customer2])

        search_results = self.controller.search_customers(self.controller.load_customers(),'Bob')

        if customer2.name in search_results and customer1.name in search_results:
            return True

    def tearDown(self):

        open('test_Customers_Data', 'w').close()

test2 = TestSearchCustomers()
test2.setUp()
test2.test_search_customers()
test2.tearDown()

class TestSearchCustomersByAddress(unittest.TestCase):
    def setUp(self):
        self.controller = RestaurantController(None, None, CustomerRepo('test_Customers_Data'), None)

    def test_search_customers_by_address(self):

        customer1 = Customer("1", 'Bob', 'Sesame Street nr. 42')
        customer2 = Customer("2", 'Bobinson', 'Wolf Street nr. 56')

        self.controller.add_customers([customer1, customer2])

        search_results = self.controller.search_customers(self.controller.load_customers(), 'Street')

        if customer2.address in search_results and customer1.address in search_results:
            return True

    def tearDown(self):
        open('test_Customers_Data', 'w').close()

test3 = TestSearchCustomersByAddress()
test3.setUp()
test3.test_search_customers_by_address()
test3.tearDown()

class TestPrintInvoice(unittest.TestCase):
    def setUp(self):
        self.dish_repo = CookedDishRepo('test_Dish_Data')
        self.drink_repo = DrinkRepo('test_Drink_Data')
        self.customer_repo = CustomerRepo('test_Customers_Data')
        self.order_repo = OrderRepo('test_Orders_Data')

        self.controller = RestaurantController(self.dish_repo, self.drink_repo, self.customer_repo, self.order_repo)

    def test_print_invoice(self):
        dish1 = Dish('1', 'Dish1', '300g', '10')
        dish2 = Dish('2', 'Dish2', '400g', '15')
        drink3 = Drink('3', 'Drink3', '200ml', '5', '3%')
        drink4 = Drink('4', 'Drink4', '300ml', '3', '2%')

        self.dish_repo.save([dish1, dish2])
        self.drink_repo.save([drink3, drink4])

        customer = Customer('1', 'Bob', 'Sesame Street')
        self.customer_repo.save([customer])

        order = Order('1', customer.id, ['1', '2'], ['3', '4'], 33)
        self.order_repo.save([order])

        retrieved_order = self.controller.find_order([order], customer.id)

        invoice = retrieved_order.call_generate_invoice(self.controller.load_dishes(), self.controller.load_drinks())
        expected_output = "Hier ist Ihre Bestellung:\n" \
                           "Dish1..................................10\n" \
                           "Dish2..................................15\n" \
                           "Drink3.................................5\n" \
                           "Drink4.................................3\n" \
                           "Ihre Gesamtkosten für die Bestellung ist 33 Euro\n" \
                           "Vielen Dank und wir warten auf Sie!\n"
        self.assertEqual(invoice,expected_output)

    def tearDown(self):
        open('test_Dish_Data', 'w').close()
        open('test_Drink_Data', 'w').close()
        open('test_Customers_Data', 'w').close()
        open('test_Orders_Data', 'w').close()

test4 = TestPrintInvoice()
test4.setUp()
test4.test_print_invoice()
test4.tearDown()
class TestAddOrder(unittest.TestCase):
    def setUp(self):
        self.order_repo = OrderRepo('test_Orders_Data')
        self.controller = RestaurantController(None, None, None, self.order_repo)

    def test_add_order(self):
        customer = Customer('1', 'Bob', 'Sesame Street')
        order = Order('1', customer.id, ['1', '2'], ['3', '4'], 30)

        self.controller.add_orders([order])

        orders_from_file = self.order_repo.load()

        for item in orders_from_file:
            assert order.id == item.id
            assert order.customer_id == item.customer_id
            assert order.drinks_id_list == item.drinks_id_list
            assert order.dishes_id_list == item.dishes_id_list

    def tearDown(self):
        open('test_Orders_Data', 'w').close()

test5 = TestAddOrder()
test5.setUp()
test5.test_add_order()
test5.tearDown()