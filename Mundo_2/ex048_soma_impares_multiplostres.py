#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
total_valores = 0
for c in range(1,501):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
        total_valores += 1
print(f"A soma de todos os {total_valores} valores soliticados é {soma}.")