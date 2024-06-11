class Order:
    def __init__(self, order_id, customer, products):
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.total_price = sum(product.price for product in products)
    
    def __orderinfo__(self):
        return f"Oder ID: {self.order_id}, Customer: {self.customer}\nTotal Price: £{self.total_spent}"
