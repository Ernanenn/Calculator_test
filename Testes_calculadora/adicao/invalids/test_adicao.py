import unittest
from calc_adicao import adicionar

class TestAdicionar(unittest.TestCase):  
    def test_adicao_string(self):
        with self.assertRaises(TypeError):
            adicionar(5, "3")

    def test_adicao_lista(self):
        with self.assertRaises(TypeError):
            adicionar(5, [1, 2, 3])

    def test_adicao_tupla(self):
        with self.assertRaises(TypeError):
            adicionar(5, (1, 2, 3))

    def test_adicao_dicionario(self):
        with self.assertRaises(TypeError):
            adicionar(5, {"a": 1, "b": 2})

    def test_adicao_none(self):
        with self.assertRaises(TypeError):
            adicionar(5, None)