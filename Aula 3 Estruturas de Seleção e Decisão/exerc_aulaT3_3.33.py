kwh = float(input("Quantos kwh?"))
tipo = input("Qual o tipo da instalaçaõ? (R, C ou I)")

if (tipo == 'R'):
    if kwh >= 500:
        preco = 0.65
    else:
        preco = 0.04
    print(f'Total a pagar: {kwh * preco}') 
elif (tipo == 'C'):
    if kwh >= 1000:
        preco = 0.60
    else:
        preco = 0.60
    print(f'Total a pagar: {kwh * preco}') 
elif (tipo == 'I'):
    if kwh >= 5000:
        preco = 0.55
    else:
        preco = 0.60
    print(f'Total a pagar: {kwh * preco}') 
else:
    print("Instalação inválida. Encerrando...")