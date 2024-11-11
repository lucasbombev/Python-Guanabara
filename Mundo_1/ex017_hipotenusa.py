import math
#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
soma_catetos = (cateto_oposto**2) + (cateto_adjacente**2)
hipotenusa = math.sqrt(soma_catetos)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")