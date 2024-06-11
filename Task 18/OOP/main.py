# manage customers by spending and threshold for VIP is 10000
# identify VIP customers if they spend more than 10000 for 1 order

from customer import Customer
from task_manager import TaskManager

# Create a TaskManager instance
task_manager = TaskManager()

# Add some customers
mike = Customer("Mike", "mike@bootcamp.com")
mike.total_spent = 3000
lily = Customer("Lily", "lily@bootcamp.com")
lily.total_spent = 7000
bill = Customer("Bill", "bill@bootcamp.com")
bill.total_spent = 8000
kathy = Customer("Kathy", "kathy@bootcamp.com")
kathy.total_spent = 15000
greg = Customer("Greg", "greg@bootcamp.com")
greg.total_spent = 20000

task_manager.add_customer(mike)
task_manager.add_customer(lily)
task_manager.add_customer(bill)
task_manager.add_customer(kathy)
task_manager.add_customer(greg)

# Identify VIP customers
vip_customers = task_manager.identify_vip_customers(threshold=10000)
for customer in vip_customers:
    print(customer)