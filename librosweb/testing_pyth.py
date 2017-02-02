import doctest


def sumar_dos_numeros(a, b):
    """Suma dos numeros y retorna su resultado

    Argumentos:
    a -- primer sumando
    b -- segundo sumando

    Test:
    >>> sumar_dos_numeros(25, 10)
    35
    >>> sumar_dos_numeros(30, 20)
    50
    """
    return a + b


if __name__ == "__main__":
    doctest.testmod()