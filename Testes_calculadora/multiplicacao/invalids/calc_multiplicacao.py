def multiplicar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Os argumentos devem ser números.")
    return a * b