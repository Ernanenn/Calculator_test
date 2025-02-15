import unittest
from calc_fatorial import fatorial

class TestFatorial(unittest.TestCase):
    def test_fatorial_menor(self):
        self.assertEqual(fatorial(1), 1)
    
    def test_fatorial_menor(self):
        self.assertEqual(fatorial(2), 2)
    
    def test_fatorial_zero(self):
        self.assertEqual(fatorial(0), 1)
    
    def test_fatorial_maior(self):
        self.assertEqual(fatorial(10), 3628800)
