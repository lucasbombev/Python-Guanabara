# Inicializa as variáveis para armazenar o produto mais barato, seu nome, o total da compra e a quantidade de produtos acima de R$1000
mais_barato = None
mais_barato_nome = None
total = 0
mais_de_mil = 0

# Exibe o cabeçalho da loja
print('-'*30)
print("LOJA SUPER BARATÃO")
print('-'*30)

# Loop principal para cadastro de produtos
while True:
    # Solicita o nome e o preço do produto
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    
    # Atualiza o total da compra
    total += preco
    
    # Verifica se o produto custa mais de R$1000 e incrementa o contador
    if preco > 1000:
        mais_de_mil += 1
    
    # Verifica se o produto é o mais barato até o momento
    if mais_barato == None or preco < mais_barato:
        mais_barato = preco
        mais_barato_nome = nome
    
    # Pergunta ao usuário se deseja continuar
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == 'N':  # Sai do loop se o usuário não quiser continuar
        break

# Exibe o resumo da compra
print("-"*10, "FIM DO PROGRAMA", "-"*10)
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {mais_de_mil} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {mais_barato_nome} que custa R${mais_barato:.2f}")