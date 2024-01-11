import unittest
from Controller.Controller import *
from Repository.DATA.DATA_REPOS import *
from Modelle.DISHES.FOOD_DRINK import *

class TestAddDish(unittest.TestCase):
    def setUp(self):
        # Set up the controller with a test repository
        self.controller = RestaurantController(CookedDishRepo('test_Dish_Data'), None, None, None)

    def test_add_cooked_dish(self):
        # Create a test CookedDish object
        test_cooked_dish = CookedDish("1", "Goulash","450g", "14", "30 Minutes")

        # Add the test CookedDish to the file
        self.controller.add_dishes([test_cooked_dish])

        # Load the dishes from the file
        loaded_dishes = self.controller.load_dishes()

        # Check if the test CookedDish is in the loaded dishes
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
        # Set up the controller with a test repository
        self.controller = RestaurantController(None, None, CustomerRepo('test_Customers_Data'), None)

    def test_search_customers(self):
        # Create test customers
        customer1 = Customer("1", 'Bob', 'Sesame Street nr. 4')
        customer2 = Customer('2', 'Bobinson', 'Wolf Street nr. 65')

        # Add test customers to the file
        self.controller.add_customers([customer1, customer2])

        # Search for customers with "Bob" in their name
        search_results = self.controller.search_customers(self.controller.load_customers(),'Bob')

        # Check if the search results contain the expected customers
        if customer2.name in search_results and customer1.name in search_results:
            return True

    def tearDown(self):
        # Clean up by removing the test file
        open('test_Customers_Data', 'w').close()

test2 = TestSearchCustomers()
test2.setUp()
test2.test_search_customers()
test2.tearDown()

import unittest
from Controller.Controller import RestaurantController
from Repository.DATA.DATA_REPOS import CustomerRepo
from Modelle.CUSTOMERS_AND_ORDERS.CUSTOMERS_ORDERS import Customer

class TestSearchCustomersByAddress(unittest.TestCase):
    def setUp(self):
        # Set up the controller with a test repository
        self.controller = RestaurantController(None, None, CustomerRepo('test_Customers_Data'), None)

    def test_search_customers_by_address(self):
        # Create test customers
        customer1 = Customer("1", 'Bob', 'Sesame Street nr. 42')
        customer2 = Customer("2", 'Bobinson', 'Wolf Street nr. 56')

        # Add test customers to the file
        self.controller.add_customers([customer1, customer2])

        # Search for customers with "Street" in their address
        search_results = self.controller.search_customers(self.controller.load_customers(), 'Street')

        # Check if the search results contain the expected customers
        if customer2.address in search_results and customer1.address in search_results:
            return True

    def tearDown(self):
        # Clean up by removing the test file
        open('test_Customers_Data', 'w').close()

test3 = TestSearchCustomersByAddress()
test3.setUp()
test3.test_search_customers_by_address()
test3.tearDown()

class TestPrintInvoice(unittest.TestCase):
    def setUp(self):
        # Set up the controller with test repositories
        self.dish_repo = CookedDishRepo('test_Dish_Data')
        self.drink_repo = DrinkRepo('test_Drink_Data')
        self.customer_repo = CustomerRepo('test_Customers_Data')
        self.order_repo = OrderRepo('test_Orders_Data')

        self.controller = RestaurantController(self.dish_repo, self.drink_repo, self.customer_repo, self.order_repo)

    def test_print_invoice(self):
        # Add test dishes, drinks, and customers to the files
        dish1 = Dish('1', 'Dish1', '300g', '10')
        dish2 = Dish('2', 'Dish2', '400g', '15')
        drink3 = Drink('3', 'Drink3', '200ml', '5', '3%')
        drink4 = Drink('4', 'Drink4', '300ml', '3', '2%')

        self.dish_repo.save([dish1, dish2])
        self.drink_repo.save([drink3, drink4])

        customer = Customer('1', 'Bob', 'Sesame Street')
        self.customer_repo.save([customer])

        # Generate an order using the added dishes, drinks, and customer
        order = Order('1', customer.id, ['1', '2'], ['3', '4'], 33)
        self.order_repo.save([order])

        # Capture the actual output by calling the print_invoice method
        retrieved_order = self.controller.find_order([order], customer.id)

        invoice = retrieved_order.call_generate_invoice(self.controller.load_dishes(), self.controller.load_drinks())
            # Check if the printed invoice matches the expected output
        expected_output = "Hier ist Ihre Bestellung:\n" \
                           "Dish1..................................10\n" \
                           "Dish2..................................15\n" \
                           "Drink3.................................5\n" \
                           "Drink4.................................3\n" \
                           "Ihre Gesamtkosten für die Bestellung ist 33 Euro\n" \
                           "Vielen Dank und wir warten auf Sie!\n"
        self.assertEqual(invoice,expected_output)

    def tearDown(self):
        # Clean up by removing the test files
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
        # Set up the controller with a test repository
        self.order_repo = OrderRepo('test_Orders_Data')
        self.controller = RestaurantController(None, None, None, self.order_repo)

    def test_add_order(self):
        # Create a test customer and order
        customer = Customer('1', 'Bob', 'Sesame Street')
        order = Order('1', customer.id, ['1', '2'], ['3', '4'], 30)

        # Add the test order to the file
        self.controller.add_orders([order])

        # Retrieve the orders from the file
        orders_from_file = self.order_repo.load()

        # Check if the added order is in its respective tuple format
        for item in orders_from_file:
            assert order.id == item.id
            assert order.customer_id == item.customer_id
            assert order.drinks_id_list == item.drinks_id_list
            assert order.dishes_id_list == item.dishes_id_list

    def tearDown(self):
        # Clean up by removing the test file
        open('test_Orders_Data', 'w').close()

test5 = TestAddOrder()
test5.setUp()
test5.test_add_order()
test5.tearDown()