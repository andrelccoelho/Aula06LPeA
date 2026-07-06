# Qual a quantidade de km percorridos por um carro alugado pelo usuário
km_dia = float(input("O carro rodou quantos Km? "))

# Qual a quatidade de dias que o carro foi alugado pelo usuário
qtde_dias = int(input("O carro foi alugado por quantos dias? "))

p_dias = qtde_dias*60
p_km = km_dia*0.15

final = p_dias + p_km

print("A quantidade de dias foi {}  e os km rodados foram {}".format (km_dia, qtde_dias))
print("O preço final dos km rodados foi {} e dos dias alugados foi {}" .format (p_km, p_dias))

# Calcule o preço a pagar => carro R$ 60,00 por dia e R$ 0,15 por km rodado

print("O preço total a ser pago foi de {}" .format(final))