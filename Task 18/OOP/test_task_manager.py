import unittest
from customer import Customer
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def test_vip_customers(self):
        # Create a TaskManager instance
        task_manager = TaskManager()

        # Create customers with different total spending
        mike = Customer("Mike", "mike@bootcamp.com")
        mike.total_spent = 3000
        lily = Customer("Lily", "lily@bootcamp.com")
        lily.total_spent = 7000
        bill = Customer("Bill", "bill@bootcamp.com")
        bill.total_spent = 8000
        kathy = Customer("Kathy", "kathy@bootcamp.com")
        kathy.total_spent = 15000
        greg = Customer("Greg", "greg@bootcamp.com")
        greg.total_spent = 16000

        # Add customers to the TaskManager
        task_manager.add_customer(mike)
        task_manager.add_customer(lily)
        task_manager.add_customer(bill)
        task_manager.add_customer(kathy)
        task_manager.add_customer(greg)

        # Identify VIP customers with a threshold of 10000
        vip_customers = task_manager.identify_vip_customers(threshold=10000)

        # Check if the correct number of customers is identified as VIP
        self.assertEqual(len(vip_customers), 2)

        # Check if each identified customer is indeed a VIP
        self.assertIn(kathy, vip_customers)
        self.assertIn(greg, vip_customers)
        self.assertNotIn(mike, vip_customers)
        self.assertNotIn(lily, vip_customers)
        self.assertNotIn(bill, vip_customers)

if __name__ == "__main__":
    unittest.main()