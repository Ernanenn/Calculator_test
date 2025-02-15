import pytest
from calc_divisao import dividir

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(5, 0)
        
def test_divisao_string():
    with pytest.raises(TypeError):
        dividir(12, "3")

def test_divisao_lista():
    with pytest.raises(TypeError):
        dividir(20, [1, 2, 4])

def test_divisao_tupla():
    with pytest.raises(TypeError):
        dividir(30, (1, 2, 3))

def test_divisão_dicionario():
        with pytest.raises(TypeError):
            dividir(8, {"a": 2, "b": 4})

def test_divisao_none():
        with pytest.raises(TypeError):
            dividir(50, None)
        
