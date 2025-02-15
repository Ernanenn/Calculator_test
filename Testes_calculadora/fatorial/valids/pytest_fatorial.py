import pytest
from calc_fatorial import fatorial

def test_fatorial_menor():
    assert fatorial(1) == 1
    
def test_fatorial_menor():
    assert fatorial(2) == 2
    
def test_fatorial_zero():
    assert fatorial(0) == 1
    
def test_fatorial_maior():
    assert fatorial(10) == 3628800
