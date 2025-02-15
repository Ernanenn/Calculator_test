import pytest
from calc_multiplicacao import multiplicar

def test_multiplicar_positivo_pequenos():
    assert multiplicar(2, 3) == 6
        
def test_multiplicar_positivo_grandes():
    assert multiplicar(150, 285) == 42750
        
def test_multiplicar_negativos():
    assert multiplicar(-8, -12) == 96
    
def test_multiplicar_misto():
    assert multiplicar(-5, 14) == -70
    
def test_multiplicar_decimais():
    assert multiplicar(3.12, 2.84) == 8.8608
    
def test_multiplicar_decimais_misto():
    assert multiplicar(1.5, -0.75) == -1.125
        
def test_multiplicar_por_zero():
    assert multiplicar(2, 0) == 0

def test_multiplicar_por_um():
    assert multiplicar(7, 1), 7
    
def test_multiplicar_por_um():
    assert multiplicar(14, -1) == -14
