import pytest
from calc_multiplicacao import multiplicar

def test_multiplicacao_por_string():
    with pytest.raises(TypeError):
        multiplicar(2, "a")

def test_multiplicacao_lista():
    with pytest.raises(TypeError):
        multiplicar(5, [1, 2, 4])

def test_multiplicacao_tupla():
    with pytest.raises(TypeError):
        multiplicar(3, (1, 2, 3))

def test_multiplicacao_dicionario():
    with pytest.raises(TypeError):
        multiplicar(11, {"a": 3, "b": 6})

def test_multiplicacao_none():
    with pytest.raises(TypeError):
        multiplicar(9, None)