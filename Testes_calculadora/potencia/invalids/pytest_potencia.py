import pytest
from calc_potencia import potencia

def test_potencia_base_zero_expoente_negativo():
    with pytest.raises(ValueError):
        potencia(0, -2)
    
def test_potencia_base_string():
    with pytest.raises(TypeError):
        potencia("a", 2)
        
def test_potencia_expoentestring():
    with pytest.raises(TypeError):
            potencia(2, "b")

        



