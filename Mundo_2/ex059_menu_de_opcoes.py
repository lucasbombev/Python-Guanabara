numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
opcao = 58
while opcao != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input("Qual é sua opção? "))
    print("-" * 30)
    match opcao:
        case 1:
            print(f"A soma entre {numero1} e {numero2} é {numero1+numero2}")
        case 2:
            print(f"A multiplicação entre {numero1} e {numero2} é {numero1*numero2}")
        case 3:
            if numero1 == numero2:
                print("Os valores são iguais!")
            else:
                maior = max(numero1, numero2)  # Ou verificar manualmente
                print(f"O maior valor é {maior}")
        case 4:
            numero1 = int(input("Digite o primeiro número: "))
            numero2 = int(input("Digite o segundo número: "))
        case 5:
            print("Finalizando...")
        case _:
            print("Digite um valor válido!")