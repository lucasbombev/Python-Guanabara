#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
continua = 's'
total = 0
conta = 0
maior = None
menor = None
while continua != 'N':
    numero = int(input("Digite um número: "))
    total += numero

    # Atualiza o maior e o menor valor
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

    continua = str(input("Quer continuar? [S/N]:").upper().strip())
    if continua != 'S' and continua != 'N':
        print("Digite um valor válido!")
    conta += 1
print(f"Você digitou {conta} números e a média foi {total/conta:.2f}")
print(f"maior:{maior}, menor{menor}")