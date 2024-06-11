# Create a task manager to manage customers by spending and threshold for VIP is 10000

class TaskManager:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def identify_vip_customers(self, threshold=10000):
        vip_customers = [customer for customer in self.customers if customer.total_spent >= threshold]
        return vip_customers