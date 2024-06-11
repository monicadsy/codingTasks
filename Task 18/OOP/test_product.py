import unittest
from product import Product

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product("diamond1", 1000)
        self.assertEqual(product.name, "diamond1")
        self.assertEqual(product.price, 1000)

    def test_product_creation(self):
        product = Product("diamond2", 2000)
        self.assertEqual(product.name, "diamond2")
        self.assertEqual(product.price, 2000)

    def test_product_creation(self):
        product = Product("diamond3", 5000)
        self.assertEqual(product.name, "diamond3")
        self.assertEqual(product.price, 5000)

    def test_product_creation(self):
        product = Product("diamond4", 6000)
        self.assertEqual(product.name, "diamond4")
        self.assertEqual(product.price, 6000)

    def test_product_creation(self):
        product = Product("diamond5", 10000)
        self.assertEqual(product.name, "diamond5")
        self.assertEqual(product.price, 10000)

if __name__ == "__main__":
    unittest.main()