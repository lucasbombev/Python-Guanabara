sexo = 'Antedeguemon'
while sexo != 'M' and sexo != 'F':
    sexo = input("informe seu sexo [M/F]: ").upper().strip()
    if sexo != 'M' or sexo != 'F':
        print("Dados inválidos, por favor,", end=' ')