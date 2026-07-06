print("Qual furta deseja comprar?")
print("1 - Maça")
print("2 - Laranja")
print("3 - Banana")
produto = int(input("Qual a sua escolha?"))
qtde = int(input("Qual a quantidade?"))
if (produto == 1):
    pagar = qtde * 2.3
    print('Você comprou {} maças. Total a pagar {}' .format(qtde, pagar))
else:
    if (produto ==2):
        pagar = qtde* 3.6
        print('Você comprou {} laranjas. Total a pagar {}' .format(qtde, pagar))
    else:
        if (produto == 3):
            pagar = qtde *1.85
            print('Você comprou {} bananas. Total a pagar {}' .format(qtde, pagar))
        else:
            print('Produto inexistente')