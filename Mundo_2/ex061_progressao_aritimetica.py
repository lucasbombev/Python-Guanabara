#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# Entrada do primeiro termo e da razão
print("Gerador de PA")
print("=" * 30)
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termo = primeiro
conta = 1
continua = 0
while conta <= 10:
    if conta < 10:
        print(f"{termo} → ", end='')
    else:
        print(termo)
    termo += razao
    conta += 1
