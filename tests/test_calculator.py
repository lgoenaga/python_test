import unittest

from src.calculator import suma, resta, multiplicacion, division

class TestCalculator(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(2, -3), -1)
        self.assertEqual(suma(-2, -3), -5)
        self.assertEqual(suma(0, 0), 0)
        self.assertEqual(suma(0, 3), 3)
        self.assertEqual(suma(3, 0), 3)
    
    def test_resta(self):
        self.assertEqual(resta(2, 3), -1)
        self.assertEqual(resta(2, -3), 5)
        self.assertEqual(resta(-2, -3), 1)
        self.assertEqual(resta(0, 0), 0)
        self.assertEqual(resta(0, 3), -3)
        self.assertEqual(resta(3, 0), 3)
    
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)
        self.assertEqual(multiplicacion(2, -3), -6)
        self.assertEqual(multiplicacion(-2, -3), 6)
        self.assertEqual(multiplicacion(0, 0), 0)
        self.assertEqual(multiplicacion(0, 3), 0)
        self.assertEqual(multiplicacion(3, 0), 0)
    
    def test_division(self):       
        self.assertEqual(division(2, 3), 2/3)
        self.assertEqual(division(2, -3), 2/-3)
        self.assertEqual(division(-2, -3), -2/-3)
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(division(0, 0), 0/0) # División por cero
        self.assertEqual(division(0, 3), 0/3)
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(division(3, 0), 3/0) # División por cero