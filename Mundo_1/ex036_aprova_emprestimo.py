#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input("Valor da casa: R$"))
salario_comprador = float(input("Salário do comprador: R$"))
anos_financiamento = int(input("Quantos anos de financiamento? "))

parcelas = valor_casa / (anos_financiamento * 12)

print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos_financiamento} anos a prestação será de {parcelas:.2f}")
if parcelas > (salario_comprador * 0.3):
    print("Emprestimo NEGADO! \nseu salário é muito baixo para pagar a parcela e viver")
else:
    print("Emprestimo CONCEDIDO!")
