import pytest
from calc_adicao import adicionar

def test_adicao_positivo():
    assert adicionar(5, 5) == 10
    
def test_adicao_zero():
    assert adicionar(5, 0) == 5

def test_adicao_negativo():
    assert adicionar(-10, -20) == -30
    
def test_adicao_decimal():
    assert adicionar(2.5, 3.7) == 6.2

def test_adicao_misto():
    assert adicionar(5, -3) == 2
    
def test_adicao_misto_decimal():
    assert adicionar(8, -0.548) == 7.452

def test_adicao_grande():
    assert adicionar(1000000, 2000000) == 3000000
