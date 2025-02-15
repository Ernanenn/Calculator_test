import unittest
from calc_fatorial import fatorial

class TestFatorial(unittest.TestCase):
    def test_fatorial_negativo(self):
        with self.assertRaises(ValueError):
            fatorial(-1)

    def test_fatorial_decimal(self):
        with self.assertRaises(ValueError):
            fatorial(3.5)

