""" Atividade feita em dupla
    Integrantes:
    - Nome: João Pedro (2022011087) 
    - Nome: Cauã Barros (20240045292)
"""

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


# --- Código para uso interativo ---
print("Conversor de Temperatura")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
opcao = int(input("Escolha a opção (1 ou 2): "))
graus = float(input("Digite o valor da temperatura: "))
resultado = conversorTemperatura(opcao, graus)
if resultado is not None:
    if opcao == 1:
        print(f"\nResultado: {resultado} graus Fahrenheit\n")
    elif opcao == 2:
        print(f"\nResultado: {resultado} graus Celsius\n")
else:
    print("Opção inválida. Escolha 1 ou 2.")