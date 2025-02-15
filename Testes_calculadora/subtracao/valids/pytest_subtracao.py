import pytest
from calc_subtracao import subtrair

def test_subtracao_positivos():
    assert subtrair(5, 3) == 2
        
def test_subtracao_positivo_negativo():
    assert subtrair(6, -3) == 9
    
def test_subtracao_negativo_positivo():
    assert subtrair(-8, 5) == -13
        
def test_subtracao_negativos():
    assert subtrair(-3, -18) == 15