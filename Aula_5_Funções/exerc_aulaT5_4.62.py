def omelete():
    ovos = 12
    print('Ovos = ', ovos)

def bacon():
    ovos = 6
    print('Ovos = ', ovos) 
    omelete()
    print('Ovos = ', ovos)

# programa principal
ovos = 2
bacon()
print('Ovos =', ovos)