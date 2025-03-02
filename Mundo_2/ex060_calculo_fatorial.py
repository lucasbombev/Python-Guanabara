'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

numero = int(input("Digite um número para saber seu fatorial: "))
contador = numero
fatorial = 1  # Inicializa com 1, pois multiplicação começa em 1
expressao = f"{numero}! = "  # String para exibir a operação

while contador > 0:
    expressao += str(contador)
    expressao += " x " if contador > 1 else " = "  # Formatação da exibição
    fatorial *= contador  # Multiplica o valor acumulado pelo contador
    contador -= 1

print(expressao + str(fatorial))