def conversorTemperatura(opcao1, graus):
    """
    >>> conversorTemperatura(1, 0)
    32.0
    >>> conversorTemperatura(1, 100)
    212.0
    >>> conversorTemperatura(2, 32)
    0.0
    >>> conversorTemperatura(2, 212)
    100.0
    """
    if opcao1 == 1:
        return graus * 9 / 5 + 32
    elif opcao1 == 2:
        return (graus - 32) * 5 / 9
    else:
        return None

import doctest
doctest.testmod()