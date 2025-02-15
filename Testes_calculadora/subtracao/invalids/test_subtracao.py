import unittest
from calc_subtracao import subtrair

class TestSubtracao(unittest.TestCase):
    def test_subtracao_string(self):
        with self.assertRaises(TypeError):
            subtrair(5, "3")

    def test_subtracao_lista(self):
        with self.assertRaises(TypeError):
            subtrair(5, [1, 2, 3])

    def test_subtracao_tupla(self):
        with self.assertRaises(TypeError):
            subtrair(5, (1, 2, 3))

    def test_subtracao_dicionario(self):
        with self.assertRaises(TypeError):
            subtrair(5, {"a": 1, "b": 2})

    def test_subtracao_none(self):
        with self.assertRaises(TypeError):
            subtrair(5, None)
