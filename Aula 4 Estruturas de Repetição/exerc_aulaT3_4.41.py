nome = '' # Falsey
while not nome: #not Falsey (ou seja, transformando em True)
    # encerra o laço quando nome não estiver vazio
    nome = input('Digite seu nome:')

valor = int(input('Digite um número qualquer:'))
if valor: #Equivalente if valor != 0:
    print('Você digitou um valor diferente de zero.')
else:
    print('Você digitou zero.')