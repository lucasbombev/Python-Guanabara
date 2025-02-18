numero = int(input("Digite um número inteiro: "))
escolha = int(input(""""Escolha uma das bases para conversão:
      [ 1 ] converter para BINÁRIO
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEXADECIMAL\n"""))

match escolha:
    case 1:
        resultado = bin(numero)[2:]
        print(f"O número {numero} em BINÁRIO é: {resultado}")
    case 2:
        resultado = oct(numero)[2:]
        print(f"O número {numero} em OCTAL é: {resultado}")
    case 3:
        resultado = hex(numero)[2:]
        print(f"O número {numero} em HEXADECIMAL é: {resultado}")
    case _:
        print("OPÇÃO INVÁLIDA!")