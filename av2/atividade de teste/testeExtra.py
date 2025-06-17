def calcularMulta(velocidade):
    """
    >>> calcularMulta(50)
    0.0
    >>> calcularMulta(60)
    0.0
    >>> calcularMulta(65)
    215.0
    >>> calcularMulta(100)
    320.0
    >>> calcularMulta(-5)
    'Velocidade inválida'
    >>> calcularMulta("rápido")cls
    'Velocidade inválida'
    """
    try:
        v = float(velocidade)
        if v < 0:
            return "Velocidade inválida"
        elif v <= 60:
            return 0.0
        else:
            excesso = v - 60
            return 200 + (excesso * 3)
    except:
        return "Velocidade inválida"

import doctest
doctest.testmod()

