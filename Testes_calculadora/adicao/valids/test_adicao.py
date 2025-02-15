import unittest
from calc_adicao import adicionar

class TestAdicionar(unittest.TestCase):
    def test_adicao_positivo(self):
        self.assertEqual(adicionar(5, 5), 10)
    
    def test_adicao_zero(self):
        self.assertEqual(adicionar(5, 0), 5)

    def test_adicao_negativo(self):
        self.assertEqual(adicionar(-10, -20), -30)
    
    def test_adicao_decimal(self):
        self.assertEqual(adicionar(2.5, 3.7), 6.2)

    def test_adicao_misto(self):
        self.assertEqual(adicionar(5, -3), 2)
    
    def test_adicao_misto_decimal(self):
        self.assertEqual(adicionar(8, -0.548), 7.452)

    def test_adicao_grande(self):
        self.assertEqual(adicionar(1000000, 2000000), 3000000)
