#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# Entrada do primeiro termo e da razão
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao , razao):
    print(f" {c} ", end=" -> ")
print("FIM")