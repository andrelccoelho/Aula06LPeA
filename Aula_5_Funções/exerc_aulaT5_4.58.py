def soma3(x=0, y=0, z=0):
    """
    Calcula a soma de até três números.

    Parâmetros padrão (=0) tornam os argumentos opcionais, evitam 
    erros de execução (TypeError) caso valores sejam omitidos e 
    usam o zero como elemento neutro para não alterar a soma.
    """
    res = x + y + z
    print(res)

# Exemplos de uso:
soma3(1, 2, 3) # Executa: 1 + 2 + 3 = 6
soma3(1, 2)    # Executa: 1 + 2 + 0 = 3 (z omitido)
soma3(1)       # Executa: 1 + 0 + 0 = 1 (y e z omitidos)
soma3()        # Executa: 0 + 0 + 0 = 0 (todos omitidos)