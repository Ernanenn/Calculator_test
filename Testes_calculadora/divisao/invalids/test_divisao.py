import unittest
from calc_divisao import dividir

class TestDividir(unittest.TestCase):
    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(5, 0)
        
    def test_divisao_string(self):
        with self.assertRaises(TypeError):
            dividir(12, "3")

    def test_divisao_lista(self):
        with self.assertRaises(TypeError):
            dividir(20, [1, 2, 4])

    def test_divisao_tupla(self):
        with self.assertRaises(TypeError):
            dividir(30, (1, 2, 3))

    def test_divisão_dicionario(self):
        with self.assertRaises(TypeError):
            dividir(8, {"a": 2, "b": 4})

    def test_divisao_none(self):
        with self.assertRaises(TypeError):
            dividir(50, None)
        
