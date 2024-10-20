#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# Solicitar informações do usuário
valor_casa = float(input("Qual é o valor da casa? R$ "))
salario = float(input("Qual é o seu salário? R$ "))
anos = int(input("Em quantos anos você vai pagar a casa? "))

# Calcular a prestação mensal
prestacao_mensal = valor_casa / (anos * 12)

# Calcular o limite de 30% do salário
limite = salario * 0.3

# Verificar se a prestação mensal é maior que 30% do salário
if prestacao_mensal <= limite:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado! A prestação mensal excede 30% do seu salário.")
