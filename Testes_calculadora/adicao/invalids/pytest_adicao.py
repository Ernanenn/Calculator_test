import pytest
from calc_adicao import adicionar

def test_adicao_string():
    with pytest.raises(TypeError):
        adicionar(5, "3")

def test_adicao_lista():
    with pytest.raises(TypeError):
        adicionar(5, [1, 2, 3])

def test_adicao_tupla():
    with pytest.raises(TypeError):
        adicionar(5, (1, 2, 3))

def test_adicao_dicionario():
    with pytest.raises(TypeError):
        adicionar(5, {"a": 1, "b": 2})

def test_adicao_none():
    with pytest.raises(TypeError):
        adicionar(5, None)