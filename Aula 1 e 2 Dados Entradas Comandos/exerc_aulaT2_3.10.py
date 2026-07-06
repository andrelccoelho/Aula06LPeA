nome = input("Qual o seu nome?")
print('Olá {}, seja bem vindo!' .format(nome))

nota = float(input("Qual nota você recebeu na dsiciplina?"))
print('Você tirou nota {}.' .format(nota))


X = int(input('Digite um número inteiro: .'))
y = int(input('Digite um número inteiro: .'))

res ='O resultado da soma de %i e com %i é %i.' % (X, y, X +y)
print(res)

#maneira moderna 
res = 'O resultado da soma de {} e com {} é {}.' .format(X, y, X +y)
print(res)
