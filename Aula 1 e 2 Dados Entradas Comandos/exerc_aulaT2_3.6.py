nota = 8.5 # Composição
s1 = 'Você tirou %f na disciplina de algoritmos' % nota
print(s1)

nota = 8.5 # Composição
s1 = 'Você tirou %.2f na disciplina de algoritmos' % nota
print(s1)

nota = 8.5 # Composição # Operador de Formatação (ou estilo printf)
disciplina = 'Algoritmos'
s1 = 'Você tirou %.2f na disciplina de %s' % (nota, disciplina) 

# f indica que o dado é um número de ponto flutuante (float/decimal).
# s indica que o dado deve ser tratado como uma string (texto).
# após a string, você coloca o operador % seguido de uma tupla (nota, disciplina)

print(s1)

nota = 8.5 # Composição # Operador de Formatação (ou estilo printf)
disciplina = 'Algoritmos'
s1 = 'Você tirou {} na disciplina de {}' .format(nota, disciplina) 
print(s1)