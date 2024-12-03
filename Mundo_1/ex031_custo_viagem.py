#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input("Qual a distância da viagem(Km)? "))
viagem_curta = distancia * 0.50
viagem_longa = distancia * 0.45
print(f"Você está preste a começar uma viagem de {distancia:.2f}km.")

if distancia <= 200:
    print(f"E o preço da sua passagem será de R$ {viagem_curta}")
else:
    print(f"E o preço da sua passagem será de R${viagem_longa}")