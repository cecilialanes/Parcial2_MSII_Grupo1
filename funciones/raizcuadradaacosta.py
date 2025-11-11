#funciones/raiz_cuadrada.py
import math

def raiz_cuadrada(x):
    """Devuelve la raíz cuadrada de un número positivo."""
    if x < 0:
        return None
    return math.sqrt(x)
