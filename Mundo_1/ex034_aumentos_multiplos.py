#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Qual o salário do funcionário? R$"))
aumento_peao_master = (salario * 0.15) + salario
aumento_peaozinho = (salario * 0.10) + salario
if salario >= 1250:
    print(f"Quem ganhava R${salario:.2f} passará a ganhar R${aumento_peaozinho}.")
else:
    print(f"Quem ganhava R${salario:.2f} passará a ganhar R${aumento_peao_master}.")
print("Lute pelos seus direitos trabalhistas!")