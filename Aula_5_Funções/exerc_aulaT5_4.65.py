def soma3(x= 0, y =0, z =0):
    res = x + y + z
    return res                    # return retorna para o principal o resultado dessa variável

# programa principal
retornado = soma3(1,2, 3)   # retornado recebe o resultado desta variável somando três números, soma 3
print(retornado)                # imprime o retornado acma

# forma alternativa simplificada
print(soma3(2,2))           # forma alternativa ao programa principal, que elimina o retornado. só que somando só 2 pq o terceiro é z = 0 e é desconsiderado

# programa principal
retornado1 = soma3(1,2,3)
retornado2 = soma3(1,2)
retornado3 = soma3()
print(f'Somatórios: {retornado1}, {retornado2} e {retornado3}.')