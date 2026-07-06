# Um aluno, para passar de ano, precisa ser aprovado em todas as matérias que está cursando.
# Assuma que a média para aprovaçaõ é a partir de 7 e que o aluno só cursa 3 matérias
# Escreva um algoritmo que leia a nota final do aluno em cada matéria e informe, na tela, se ele passou ou não

m1 = float(input('Digite a nota da matéria 1: '))
m2 = float(input('Digite a nota da matéria 1: '))
m3 = float(input('Digite a nota da matéria 1: '))
if m1 >= 7 and m2 >= 7 and m3 >= 7:
    print('O aluno está aprovado!');
else:
    print('O aluno não passou de ano!');