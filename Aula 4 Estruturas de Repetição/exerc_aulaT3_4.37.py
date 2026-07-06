soma = 0
cont = 1
while (cont <= 5):
    x = int(input(f'Digite o {cont}º número:'))
    soma += x # Equivalente: soma = soma + x
    cont += 1 # Equivalente: cont = cont + 1
print(f'Somatório: {soma}')