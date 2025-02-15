import unittest
from calc_potencia import potencia

class TestPotencia(unittest.TestCase):
    def test_potencia_base_zero_expoente_negativo(self):
        with self.assertRaises(ValueError):
            potencia(0, -2)
    
    def test_potencia_base_string(self):
        with self.assertRaises(TypeError):
            potencia("a", 2)
        
    def test_potencia_expoentestring(self):
        with self.assertRaises(TypeError):
            potencia(2, "b")

        



