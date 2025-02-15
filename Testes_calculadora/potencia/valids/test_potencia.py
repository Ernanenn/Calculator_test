import unittest
from calc_potencia import potencia
import math

class TestPotencia(unittest.TestCase):
    def test_potenciacao_positivos(self):
        self.assertEqual(potencia(2, 3), 8)
    
    def test_potenciacao_base_negativa(self):
        self.assertEqual(potencia(-2, 4), 16)
    
    def test_potenciacao_base_negativa(self):
        self.assertEqual(potencia(-2, -3), -0.125)
    
    def test_potenciacao_base_zero(self):
        self.assertEqual(potencia(0, 2), 0)
    
    def test_potenciacao_expoente_zero(self):
        self.assertEqual(potencia(5, 0), 1)
        
    def test_potenciacao_expoente_um(self):
        self.assertEqual(potencia(5, 1), 5)
    
    def test_potenciacao_base_um(self):
        self.assertEqual(potencia(1, 3), 1)
    
    def test_potenciacao_base_negativa_expoente_decimal(self):
        self.assertEqual(potencia(-6, 0.5), 1.4998798865218462e-16+2.449489742783178j)
    
    def test_potenciacao_base_decimal_expoente_inteiro(self):
        self.assertEqual(potencia(2.5, 4), 39.0625)
    
    def test_potenciacao_base_decimal_expoente_decimal(self):
        self.assertEqual(potencia(1.5, 3.5), 4.133513940946613)
