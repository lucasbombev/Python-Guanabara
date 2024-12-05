'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:4
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal
3x ou mais no cartão: 20% de juros'''
compras = float(input("Preço das compras: R$:"))
#choice1 
preco_avista = compras - (compras * 0.1) 
#choice2
preco_vencimento = compras - (compras * 0.05)
#choice3
preco_2x = compras
#choice4 
preco_3x = compras + (compras * 0.2)
escolha_pagamento = int(input(('''   FORMAS DE PAGAMENTO
      [ 1 ] à vista
      [ 2 ] vencimento
      [ 3 ] 2x crédito
      [ 4 ] 3x ou mais crédito
      ''')))

if escolha_pagamento == 1:
    print(f"Suas compras no valor de R$:{compras:.2f} com desconto de á vista 10% terão o valor final de R$:{preco_avista:.2f}.")
elif escolha_pagamento == 2:
    print(f"Suas compras no valor de R$:{compras:.2f} com desconto de 5% no vencimento terão o valor final de R$:{preco_vencimento:.2f}.")
elif escolha_pagamento == 3:
    print(f"Suas compras no valor de R$:{compras:.2f} ficará com valor formal em 2x no cartão R$:{preco_2x:.2f}.")
elif escolha_pagamento == 4:
    print(f"Suas compras no valor de R$:{compras:.2f} parcelada em 3x ou mais terá o valor final de R$:{preco_3x:.2f}.")
else:
    print("Opção Inválida!")