import unittest
from calc_multiplicacao import multiplicar

class TestMultiplicar(unittest.TestCase):
    def test_multiplicacao_por_string(self):
        with self.assertRaises(TypeError):
            multiplicar(2, "a")

    def test_multiplicacao_lista(self):
        with self.assertRaises(TypeError):
            multiplicar(5, [1, 2, 4])

    def test_multiplicacao_tupla(self):
        with self.assertRaises(TypeError):
            multiplicar(3, (1, 2, 3))

    def test_multiplicacao_dicionario(self):
        with self.assertRaises(TypeError):
            multiplicar(11, {"a": 3, "b": 6})

    def test_multiplicacao_none(self):
        with self.assertRaises(TypeError):
            multiplicar(9, None)