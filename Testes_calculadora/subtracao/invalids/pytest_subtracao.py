import pytest
from calc_subtracao import subtrair

def test_subtracao_string():
    with pytest.raises(TypeError):
        subtrair(5, "3")

def test_subtracao_lista():
    with pytest.raises(TypeError):
        subtrair(5, [1, 2, 3])

def test_subtracao_tupla():
    with pytest.raises(TypeError):
        subtrair(5, (1, 2, 3))

def test_subtracao_dicionario():
    with pytest.raises(TypeError):
        subtrair(5, {"a": 1, "b": 2})

def test_subtracao_none():
    with pytest.raises(TypeError):
        subtrair(5, None)
