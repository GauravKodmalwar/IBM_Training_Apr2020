import unittest
from Customer import Cars, RetailCar

retail = RetailCar("Retail", "Petrol", "Tata", 18, 4)
retail.update("CNG", 100)
b, a = retail.get()
class Testing(unittest.TestCase):
    def test_string(self):
        obj = Cars("Commercial", "Diesel", "Tata")
        self.assertEqual(obj.get(), "Diesel")
    def test_boolean(self):
        self.assertEqual(a, "Retail")
    def test_boolean2(self):
        self.assertEqual(b, 100)
    def test_boolean3(self):
        self.assertFalse(5 > 10)

if __name__ == '__main__':
    unittest.main()