import unittest
from calc_subtracao import subtrair

class TestSubtracao(unittest.TestCase):
    def test_subtracao_positivos(self):
        self.assertEqual(subtrair(5, 3), 2)
        
    def test_subtracao_positivo_negativo(self):
        self.assertEqual(subtrair(6, -3), 9)
    
    def test_subtracao_negativo_positivo(self):
        self.assertEqual(subtrair(-8, 5), -13)
        
    def test_subtracao_negativos(self):
        self.assertEqual(subtrair(-3, -18), 15)
