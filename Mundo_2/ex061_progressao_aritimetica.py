#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# Entrada do primeiro termo e da razão
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
decimo = primeiro + (10 - 1) * razao
conta = 0 

for c in range(primeiro, decimo + razao , razao):
    print(f" {c} ", end=" -> ")
print("FIM")