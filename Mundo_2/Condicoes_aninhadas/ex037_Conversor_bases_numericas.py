# Pede ao usuário para digitar um número inteiro e converte para um número
numero = int(input("Digite um número inteiro: "))

# Inicializa a variável 'option' com 0
option = 0

# Exibe opções de conversão para o usuário
print("[    1   ] converter para binário")
print("[    2   ] converter para octal")
print("[    3   ] converter para hexadecimal")

# Pede ao usuário para escolher uma opção e converte para número inteiro
option = int(input("Sua opção: "))

# Verifica se a opção escolhida é 1, 2 ou 3 e realiza a conversão correspondente
if option == 1:
    print(f"{numero} convertido para binário é {bin(numero)[2:]}")
elif option == 2:
    print(f"{numero} convertido para octal é {oct(numero)[2:]}")
elif option == 3:
    print(f"{numero} convertido para hexadecimal é {hex(numero)[2:]}")
else:
    # Se a opção não for válida, exibe uma mensagem de erro
    print("Escolha uma opção válida!")
