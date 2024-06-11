import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    def test_customer_creation(self):
        customer = Customer("Mike", "mike@bootcamp.com")
        self.assertEqual(customer.name, "Mike")
        self.assertEqual(customer.email, "mike@bootcamp.com")
        self.assertEqual(customer.total_spent, 3000)

    def test_customer_creation(self):
        customer = Customer("Lily", "lily@bootcamp.com")
        self.assertEqual(customer.name, "Lily")
        self.assertEqual(customer.email, "lily@bootcamp.com")
        self.assertEqual(customer.total_spent, 7000)
    
    def test_customer_creation(self):
        customer = Customer("Bill", "bill@bootcamp.com")
        self.assertEqual(customer.name, "Bill")
        self.assertEqual(customer.email, "bill@bootcamp.com")
        self.assertEqual(customer.total_spent, 8000)

    def test_customer_creation(self):
        customer = Customer("Kathy", "kathy@bootcamp.com")
        self.assertEqual(customer.name, "Kathy")
        self.assertEqual(customer.email, "kathy@bootcamp.com")
        self.assertEqual(customer.total_spent, 15000)

    def test_customer_creation(self):
        customer = Customer("Greg", "greg@bootcamp.com")
        self.assertEqual(customer.name, "Greg")
        self.assertEqual(customer.email, "greg@bootcamp.com")
        self.assertEqual(customer.total_spent, 20000)

if __name__ == "__main__":
    unittest.main()