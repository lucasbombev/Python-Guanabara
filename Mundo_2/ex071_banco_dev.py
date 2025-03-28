# Simulador de Caixa Eletrônico
# Solicita ao usuário o valor a ser sacado
valor = int(input("Qual valor você quer sacar? R$"))

# Inicializa as cédulas disponíveis
cedulas = [50, 20, 10, 1]  # Lista com os valores das cédulas disponíveis
indice = 0  # Índice para percorrer a lista de cédulas

print("Você receberá:")

# Processa o valor a ser sacado
while True:
    cedula_atual = cedulas[indice]  # Seleciona a cédula atual
    quantidade = valor // cedula_atual  # Calcula quantas cédulas do valor atual são necessárias
    
    if quantidade > 0:  # Exibe apenas as cédulas que serão entregues
        print(f"{quantidade} cédula(s) de R${cedula_atual}")
    
    valor %= cedula_atual  # Atualiza o valor restante a ser sacado
    
    if valor == 0:  # Se o valor restante for zero, encerra o loop
        break
    
    indice += 1  # Passa para a próxima cédula