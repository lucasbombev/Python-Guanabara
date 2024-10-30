#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Qual o salário do funcionário? R$"))
reajustado = salario * 1.15
print(f"Um funcionário que ganhava R${salario} com 15% de aumento, passa a receber R${reajustado:.2f}.")