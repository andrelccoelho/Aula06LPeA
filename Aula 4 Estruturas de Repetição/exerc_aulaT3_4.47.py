1   soma = 0
2   qtd = 0
3   for i in range(1,101):
4       if (i % 2 == 0):
5           soma += i
6           qtd += 1
7   media = soma / qtd
8   print(f'A média dos pares de 1 até 100 é: {media}') 