import math


def areaTriangulo(base, altura):
    """
    (number,number) -> numbers

    Retorna a area de um triangulo, dadas a base e a altura do mesmo.

    Exemplo:
        >>> areaTriangulo (10,5)
        ... 25,0

    """
    return base * altura / 2


def areaCirculo(raio):
    """
    (number)
    retorna a area do circulo inserindo o raio .
    é igual a pji x raio ao quadrado
    exemplo area circulo (5)
    """
    return math.pi * raio**2


def areaQuadrado(lado):
    """
    (number)
    retorna a area do quadrado inserindo os lados .
    é igual a pji x raio ao quadrado
    exemplo area quadrado (5)
    """
    return lado**2


areaTriangulo(5, 10)
