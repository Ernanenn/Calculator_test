import pytest
from calc_divisao import dividir

def test_divisao_inteiros_positivo():
    assert dividir(10, 5) == 2
        
def test_divisao_inteiros_negativos():
    assert dividir(-12, -4) == 3
        
def test_divisao_inteiros_positivos_negativos():
    assert dividir(-15, 3) == -5
    
def test_divisao_decimais():
    assert dividir(3.5, 0.5) == 7
    
def test_divisao_decimais_mistos():
    assert dividir(16, 1.5) == 10.666666666666666
    
def test_divisao_por_um():
    assert dividir(20, 1) == 20
    
def test_divisao_por_menos_um():
    assert dividir(8, -1) == -8
        
