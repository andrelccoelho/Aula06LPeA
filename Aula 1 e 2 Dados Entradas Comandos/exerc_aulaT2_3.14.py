preco = float(input("Qual o preço do produto?"))
p = float(input("Digitie o percentual do desconto (0-100): "))

desconto = preco * (p/100)
final = preco - desconto

print("O preço final é {} e o desconto foi de {}" .format(final, p))
print("Valor calculado de desconto: {}. Valor final do produto: {}". format(desconto, final))