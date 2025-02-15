import pytest
from calc_fatorial import fatorial

def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-1)

def test_fatorial_decimal():
    with pytest.raises(ValueError):
        fatorial(3.5)

