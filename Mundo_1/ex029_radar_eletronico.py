#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input("Qual a velocidade atual do carro? "))
multa = (velocidade - 80) * 7

if velocidade < 80:
    print("Tenha um bom dia! Dirija com segurança!")
else:
    print(f"MULTADO! Você excedeu o limite permitido que é de 80Km/h você deve pagar uma multa de R${multa:.2f}!")