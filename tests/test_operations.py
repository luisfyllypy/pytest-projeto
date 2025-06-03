import pytest
from calculadora.operations import (
    soma,
    subtrai,
    multiplica,
    divide,
    potencia,
    raiz_quadrada,
)

# 1. Parametrização de soma, subtração e multiplicação
@pytest.mark.parametrize(
    "x, y, esperado",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0.5, 0.25, 0.75),
        (-2.5, -2.5, -5),
    ],
    ids=["2+3", "-1+1", "0.5+0.25", "-2.5-2.5"],
)
@pytest.mark.smoke
def test_soma_parametrizado(x, y, esperado):
    assert soma(x, y) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "x, y, esperado",
    [
        (5, 2, 3),
        (0, 10, -10),
        (-3, -2, -1),
        (2.5, 1.5, 1.0),
    ],
)
def test_subtrai_parametrizado(x, y, esperado):
    assert subtrai(x, y) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "x, y, esperado",
    [
        (2, 3, 6),
        (-1, 5, -5),
        (0.5, 4, 2.0),
        (-2, -2, 4),
    ],
)
def test_multiplica_parametrizado(x, y, esperado):
    assert multiplica(x, y) == pytest.approx(esperado)


# 2. Teste de divisões incluíndo exceção em divisão por zero
@pytest.mark.parametrize(
    "x, y, esperado",
    [
        (10, 2, 5),
        (7, 2, 3.5),
        (0, 5, 0),
    ],
)
def test_divide_valores_validos(x, y, esperado):
    assert divide(x, y) == pytest.approx(esperado)

def test_divide_por_zero_levanta_valueerror():
    with pytest.raises(ValueError) as excinfo:
        divide(5, 0)
    assert "Não é possível dividir por zero" in str(excinfo.value)


# 3. Teste de potenciação (sem exceções previstas)
@pytest.mark.parametrize(
    "x, y, esperado",
    [
        (2, 3, 8),
        (5, 0, 1),
        (2.5, 2, 6.25),
        (-3, 3, -27),
    ],
)
def test_potencia_parametrizado(x, y, esperado):
    assert potencia(x, y) == pytest.approx(esperado)


# 4. Teste de raiz quadrada, incluindo exceção para valor negativo
@pytest.mark.parametrize("x, esperado", [(4, 2), (1, 1), (2.25, 1.5)])
def test_raiz_quadrada_valores_validos(x, esperado):
    assert raiz_quadrada(x) == pytest.approx(esperado)

def test_raiz_quadrada_valor_negativo_levanta_valueerror():
    with pytest.raises(ValueError) as excinfo:
        raiz_quadrada(-9)
    assert "Não é possível extrair raiz quadrada de número negativo" in str(excinfo.value)
