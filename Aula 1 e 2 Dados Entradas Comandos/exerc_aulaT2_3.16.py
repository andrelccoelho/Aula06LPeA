palavra1 = input("Qual a maior palavra da língua portuguesa que você conhece?")
tam = len(palavra1)

palavra2 = palavra1 [:int(tam/2)]

# Esse print abaixo foi adicionado só por curiosidade
print(palavra2)

# Essa é a solução
print(palavra2[-2:])