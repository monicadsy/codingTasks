import csv
from customer import Customer
from product import Product
from order import Order

class DataAccess:
    def read_customers(file_path):
        customers = []
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customer = Customer(row['Name'], row['Email'])
                customer.total_spent = float(row.get('Total Spent', 0))
                customers.append(customer)
        return customers

    def read_products(file_path):
        products = []
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product = Product(row['Name'], float(row['Price']))
                products.append(product)
        return products

    def read_orders(file_path, customers, products):
        orders = []
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customer = next((c for c in customers if c.name == row['Customer']), None)
                if customer is None:
                    raise ValueError(f"Customer '{row['Customer']}' not found.")
                
                product_names = row['Products'].split(',')
                order_products = [next((p for p in products if p.name == name), None) for name in product_names]
                if None in order_products:
                    raise ValueError(f"One or more products in order '{row['Order ID']}' not found.")

                order = Order(int(row['Order ID']), customer, order_products)
                orders.append(order)
        return orders