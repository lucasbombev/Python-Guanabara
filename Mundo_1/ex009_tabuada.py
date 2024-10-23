#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input("Digite um numero para ver sua tabuada: "))
for c in range (1,11):
    print(f"{numero} x {c} = {numero * c}")