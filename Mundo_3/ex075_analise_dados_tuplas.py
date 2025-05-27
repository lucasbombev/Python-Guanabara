'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

# Lendo quatro valores e armazenando em uma tupla
numeros = (
    int(input("Digite o primeiro número: ")),
    int(input("Digite o segundo número: ")),
    int(input("Digite o terceiro número: ")),
    int(input("Digite o quarto número: "))
)

# A) Quantas vezes apareceu o valor 9
print(f"\nO valor 9 apareceu {numeros.count(9)} vezes")

# B) Em que posição foi digitado o primeiro valor 3
if 3 in numeros:
    print(f"O valor 3 apareceu na {numeros.index(3) + 1}ª posição")
else:
    print("O valor 3 não foi digitado")

# C) Quais foram os números pares
pares = [num for num in numeros if num % 2 == 0]
if pares:
    print(f"Os números pares digitados foram: {pares}")
else:
    print("Não foram digitados números pares")