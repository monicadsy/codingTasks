# For 1) - 3) follow the Project set-up guide
# VIP client management by the spendings for an online shop

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.total_spent = 0
    
    def __customerinfo__(self):
        return f"Customer details: {self.name}, ({self.email})\nTotal Sepnt: £{self.total_spent}"


