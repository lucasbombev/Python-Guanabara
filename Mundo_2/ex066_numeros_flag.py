#Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
soma = numeros = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    numeros += 1
    soma = n + soma
print(f'Você digitou {numeros} números e a soma deles é {soma}.')
