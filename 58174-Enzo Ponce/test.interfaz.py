import unittest
from interfaz_hexa_deci import check 

class ErrorFromInput(unittest.TestCase):
    def test_1(self):
        ans = check('5')
        self.assertEqual(ans,'5')
    def test_2(self):
        ans = check(None)
        self.assertEqual(ans,'ERROR')
    def test_3(self):
        ans = check('HOLA MUNDO')
        self.assertEqual(ans,'ERROR')

if __name__ == "__main__":
    unittest.main()
