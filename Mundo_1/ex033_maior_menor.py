#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
primeiro = int(input("Primeiro valor:"))
segundo = int(input("Segundo valor:"))
terceiro = int(input("Terceiro valor:"))
maior = 0
menor = 0
#verifica maior
if primeiro > segundo and primeiro > terceiro:
    maior = primeiro
elif segundo > primeiro and segundo > terceiro:
    maior = segundo
else: 
    maior = terceiro

#verifica menor
if primeiro < segundo and primeiro < terceiro:
    menor = primeiro
elif segundo < primeiro and segundo < terceiro:
    menor = segundo
else: 
    menor = terceiro
print(f"O maior valor digitado foi {maior}")
print(f"O menor valor digitado foi {menor}")

#descobri as funções max e min mas vou deixar com a solução inicial para historicidade