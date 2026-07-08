"""
Exercício: Sistema de Bilheteria com Acumulador de Idades

Este programa simula o funcionamento de uma bilheteria. Ele lê a idade de múltiplos
visitantes em um loop contínuo até que a idade '0' seja digitada (condição de parada).
O programa calcula o preço do ingresso com base na idade, acumula o faturamento total,
conta o número de pessoas e calcula a média ao final.

Regras de Preço do Ingresso:
- Idade menor que 3 anos: R$ 0 (Gratuito)
- Idade maior que 12 anos: R$ 30
- Idade entre 3 e 12 anos: R$ 15
"""

# Inicialização dos contadores e acumuladores
total = 0          # Conta o total de pessoas que passaram pela bilheteria
dinheiro = 0       # Acumula o valor total em dinheiro dos ingressos vendidos
acc_idades = 0     # Acumula a soma das idades de todas as pessoas (útil para estatísticas de idade)

# Loop infinito para leitura contínua de dados
while True:
    idade = int(input("Qual sua idade? "))
    
    # Condição de parada: se o usuário digitar 0, sai do loop imediatamente
    if idade == 0:
        break

    # Atualização dos acumuladores a cada nova pessoa válida inserida
    total += 1
    acc_idades += idade
    
    # Estrutura condicional aninhada para definir o preço do ingresso por faixa etária
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
            
    # Soma o valor do ingresso atual ao total arrecadado no caixa
    dinheiro += ingresso

# Bloco de exibição dos resultados (só executa se pelo menos uma pessoa foi registrada)
if total > 0:
    # Nota: Usar 'acc_idades / total' calcula a média de IDADE das pessoas.
    # Para calcular a média de DINHEIRO por pessoa, o correto seria usar 'dinheiro / total'.
    media = acc_idades / total
    
    print(f"Total de pessoas: {total}")
    print(f"Total arrecadado: {dinheiro}")
    print(f"Média arrecadada: {media}") 