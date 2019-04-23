import unittest 
from decimal_hexa import decimal_hexadecimal

class TestDecimalHexa(unittest.TestCase):
    def test_1_decimal_hexa(self):
        decimal = decimal_hexadecimal(4095)
        self.assertEqual(decimal,'FFF')
    def test_2_decimal_hexa(self):
        decimal = decimal_hexadecimal(16)
        self.assertEqual(decimal,'10')
    def test_3_decimal_hexa(self):
        decimal = decimal_hexadecimal(1234)
        self.assertEqual(decimal,'4D2')
    def test_4_decimal_hexa(self):
        decimal = decimal_hexadecimal(234)
        self.accertEqual(decimal,'EA')
    def test_5_decimal_hexa(self):
        decimal = decimal_hexadecimal(921)
        self.assertEqual(decimal,'399')

if __name__ == '__main__':
    unittest.main()
             