import unittest
from customer import Customer
from product import Product
from order import Order

class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        customer = Customer("Mike", "mike@bootcamp.com")
        products = [Product("diamond1", 1000), Product("diamond2", 2000)]
        order = Order(1, customer, products)
        self.assertEqual(order.order_id, 1)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.products, products)
        self.assertEqual(order.total_price, 3000)

    def test_order_creation(self):
        customer = Customer("Lily", "lily@bootcamp.com")
        products = [Product("diamond2", 2000), Product("diamond3", 5000)]
        order = Order(2, customer, products)
        self.assertEqual(order.order_id, 2)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.products, products)
        self.assertEqual(order.total_price, 7000)

    def test_order_creation(self):
        customer = Customer("Bill", "bill@bootcamp.com")
        products = [Product("diamond2", 2000), Product("diamond4", 6000)]
        order = Order(3, customer, products)
        self.assertEqual(order.order_id, 3)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.products, products)
        self.assertEqual(order.total_price, 8000)

    def test_order_creation(self):
        customer = Customer("Kathy", "kathy@bootcamp.com")
        products = [Product("diamond3", 5000), Product("diamond5", 10000)]
        order = Order(4, customer, products)
        self.assertEqual(order.order_id, 4)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.products, products)
        self.assertEqual(order.total_price, 15000)

    def test_order_creation(self):
        customer = Customer("Greg", "greg@bootcamp.com")
        products = [Product("diamond5", 10000), Product("diamond5", 10000)]
        order = Order(5, customer, products)
        self.assertEqual(order.order_id, 5)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.products, products)
        self.assertEqual(order.total_price, 20000)

if __name__ == "__main__":
    unittest.main()