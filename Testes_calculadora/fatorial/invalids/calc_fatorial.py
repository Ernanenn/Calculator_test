def fatorial(n):
    if not isinstance(n, int):
        raise ValueError("O fatorial é definido apenas para números inteiros não negativos.")
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

