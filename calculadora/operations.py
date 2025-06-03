import math
from typing import Union

Number = Union[int, float]

def soma(x: Number, y: Number) -> Number:
    """Retorna a soma de x e y."""
    return x + y

def subtrai(x: Number, y: Number) -> Number:
    """Retorna x menos y."""
    return x - y

def multiplica(x: Number, y: Number) -> Number:
    """Retorna a multiplicação de x e y."""
    return x * y

def divide(x: Number, y: Number) -> float:
    """
    Retorna a divisão de x por y.
    Lança ValueError se y for zero.
    """
    if y == 0:
        raise ValueError("Não é possível dividir por zero")
    return x / y

def potencia(x: Number, y: Number) -> Number:
    """
    Retorna x elevado à potência y.
    Exemplo: potencia(2, 3) == 8
    """
    return x ** y

def raiz_quadrada(x: Number) -> float:
    """
    Retorna a raiz quadrada de x.
    Lança ValueError se x for negativo.
    """
    if x < 0:
        raise ValueError("Não é possível extrair raiz quadrada de número negativo")
    return math.sqrt(x)
