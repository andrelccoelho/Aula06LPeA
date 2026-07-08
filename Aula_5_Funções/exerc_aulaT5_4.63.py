def omelete():
    global ovos
    ovos = 6
    bacon()

def bacon():
    ovos = 12
    pimenta()

def pimenta():
    print(ovos)

# Programa principal
ovos = 4
omelete()
print(ovos)