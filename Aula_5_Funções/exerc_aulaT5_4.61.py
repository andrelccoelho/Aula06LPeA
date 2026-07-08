def omelete():
    ovos = 12 # variável local
    bacon() # direciona para a função "def bacon()"
    print(ovos) # agora que foi executado "omelete()" no programa principal, vai para o programa principal para executar bacon()

def bacon():
    ovos = 6 
    print(ovos) # quando termina volta para a função omelete em "print(ovos)"

# Programa principal
omelete()
bacon()