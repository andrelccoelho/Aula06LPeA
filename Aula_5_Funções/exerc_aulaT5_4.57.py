# ==============================================================================
# O GRANDE LABORATÓRIO DAS FUNÇÕES (Bloco 'def')
# ==============================================================================

def sub2(x, y):
    """
    MÁQUINA 'sub2': Uma estrutura criada dentro do grande laboratório 'def'.
    
    Buracos de entrada (Parâmetros):
      - x: O primeiro buraco, onde você joga o valor que sofrerá a subtração.
      - y: O segundo buraco, onde você joga o valor que será subtraído.
    """
    # GAVETA INTERNA 'res':
    # A máquina pega o que entrou por 'x' e 'y', faz a conta de subtração
    # e guarda o resultado temporariamente nesta gaveta secreta chamada 'res'.
    res = x - y
    
    # VISOR DA MÁQUINA 'print':
    # Abre a gaveta 'res' e mostra o resultado final na tela para o usuário.
    print(res)


# ==============================================================================
# O MUNDO EXTERIOR (Programa Principal)
# ==============================================================================
# Aqui fora, nós não vemos o que tem dentro da máquina (como a gaveta 'res').
# Só conseguimos ver a carcaça da máquina e chamar ela pelo seu nome de fábrica: 'sub2'.

# ATIVANDO A MÁQUINA:
# Chamamos 'sub2' e chutamos os números 5 e 7 para dentro dos buracos de entrada.
# O número 5 entra no buraco 'x' e o número 7 entra no buraco 'y'.
sub2(5, 7)