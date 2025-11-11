from funciones.potencia_peveri import potencia_peveri

def test_potencia_peveri_casos_basicos():
    # Caso 1: exponente positivo
    assert potencia_peveri(2, 3) == 8

    # Caso 2: exponente cero
    assert potencia_peveri(5, 0) == 1

    # Caso 3: base negativa
    assert potencia_peveri(-2, 3) == -8

    # Caso 4: exponente negativo
    assert round(potencia_peveri(2, -2), 2) == 0.25

    # Caso 5: base decimal
    assert round(potencia_peveri(2.5, 2), 2) == 6.25
