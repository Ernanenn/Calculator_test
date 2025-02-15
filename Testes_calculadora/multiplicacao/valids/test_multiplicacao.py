import unittest
from calc_multiplicacao import multiplicar

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar_positivo_pequenos(self):
        self.assertEqual(multiplicar(2, 3), 6)
        
    def test_multiplicar_positivo_grandes(self):
        self.assertEqual(multiplicar(150, 285), 42750)
        
    def test_multiplicar_negativos(self):
        self.assertEqual(multiplicar(-8, -12), 96)
    
    def test_multiplicar_misto(self):
        self.assertEqual(multiplicar(-5, 14), -70)
    
    def test_multiplicar_decimais(self):
        self.assertEqual(multiplicar(3.12, 2.84), 8.8608)
    
    def test_multiplicar_decimais_misto(self):
        self.assertEqual(multiplicar(1.5, -0.75), -1.125)
        
    def test_multiplicar_por_zero(self):
        self.assertEqual(multiplicar(2, 0), 0)
    
    def test_multiplicar_por_um(self):
        self.assertEqual(multiplicar(7, 1), 7)
    
    def test_multiplicar_por_um(self):
        self.assertEqual(multiplicar(14, -1), -14)
