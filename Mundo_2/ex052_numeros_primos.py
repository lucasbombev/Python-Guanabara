#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input("Digite um número: "))
divisibilidade = 0

#quantas vezes foi divisível
for c in range(1, numero+1):
    if numero % c == 0:
        divisibilidade+=1
        print(f"\033[32m{c}\033[0m", end=' ')
    else:
        print(f"\033[31m{c}\033[0m", end=' ')
print(f"\nO número {numero} foi divisível {divisibilidade} vezes")
if divisibilidade > 2:
    print("E por isso ele NÃO É PRIMO")
else:
    print("E por isso ele É PRIMO!")

'''verifica_primo
verifica primo, desconsiderar pois se o número for divisível mais do que duas vezes ele não é primo. mas vou manter o código para fins de esforço e lógica

if numero <= 1:
    print("NÃO É PRIMO!")
elif numero % 2 == 0 and numero > 2:
    print("NÃO É PRIMO!")
else: 
    print("É PRIMO!")
'''    