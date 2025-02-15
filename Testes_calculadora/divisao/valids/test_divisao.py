import unittest
from calc_divisao import dividir

class TestDividir(unittest.TestCase):
    def test_divisao_inteiros_positivo(self):
        self.assertEqual(dividir(10, 5), 2)
        
    def test_divisao_inteiros_negativos(self):
        self.assertEqual(dividir(-12, -4), 3)
        
    def test_divisao_inteiros_positivos_negativos(self):
        self.assertEqual(dividir(-15, 3), -5)
    
    def test_divisao_decimais(self):
        self.assertEqual(dividir(3.5, 0.5), 7)
    
    def test_divisao_decimais_mistos(self):
        self.assertEqual(dividir(16, 1.5), 10.666666666666666)
    
    def test_divisao_por_um(self):
        self.assertEqual(dividir(20, 1), 20)
    
    def test_divisao_por_menos_um(self):
        self.assertEqual(dividir(8, -1), -8)
        
