def potencia(base, expoente):

    if not isinstance(base, (int, float)) or not isinstance(expoente, (int, float)):
        raise TypeError("Base e expoente devem ser números.")

    if base == 0 and expoente < 0:
        raise ValueError("Divisão por zero não é permitida.")
    

    return base ** expoente