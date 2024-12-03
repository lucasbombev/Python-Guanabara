#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("-=" * 30)
print("Analisador de Triângulos")
print("-=" * 30)

# Entrada dos comprimentos das três retas
primeiro_segmento = float(input("Digite o primeiro segmento: "))
segundo_segmento = float(input("Digite o segundo segmento: "))
terceiro_segmento = float(input("Digite o terceiro segmento: "))

# Verifica a condição de existência de um triângulo
if primeiro_segmento + segundo_segmento > terceiro_segmento and primeiro_segmento + terceiro_segmento > segundo_segmento and segundo_segmento + terceiro_segmento > primeiro_segmento:
    print("As retas podem formar um triângulo!")
else:
    print("As retas NÃO podem formar um triângulo.")