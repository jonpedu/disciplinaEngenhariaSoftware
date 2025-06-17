""" Atividade feita em dupla
    Integrantes:
    - Nome: João Pedro (2022011087) 
    - Nome: Cauã Barros (20240045292)
"""

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
    >>> calcularMulta("rápido")
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

# --- Código para uso interativo ---
print("Calculadora de Multa por Excesso de Velocidade")
vel = input("Digite a velocidade do veículo (km/h): ")
resultado = calcularMulta(vel)
if resultado == 0.0:
    print("\nSem multa. Velocidade dentro do limite.\n")
elif resultado == "Velocidade inválida":
    print("\nVelocidade inválida. Por favor, digite um valor numérico positivo.\n")
else:
    print(f"\nValor da multa: R$ {resultado:.2f}\n")

