def borda(s1):
    tam = len(s1)
    # só imprime caso exista algum caractere 
    if tam:
    # if tam: funciona devido a um conceito chamado Implicit Truthiness - qualquer valor ou objeto pode ser avaliado em um contexto condicional (como um if) como sendo "Verdadeiro" (True) ou "Falso" (False).
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

# Programa Principal
borda('Olá, Mundo!')
borda('Lógica de Programação e Algoritmos')