#tests/test_raiz_cuadrada.py
from funciones.raiz_cuadrada import raiz_cuadrada

def test_raiz_cuadrada():
    assert raiz_cuadrada(9) == 3
    assert raiz_cuadrada(-4) is None