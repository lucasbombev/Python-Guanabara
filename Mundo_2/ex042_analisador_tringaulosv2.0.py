'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes'''

print("-=" * 30)
print("Analisador de Triângulos 2.0")
print("-=" * 30)

# Entrada dos comprimentos das três retas
primeiro_segmento = float(input("Digite o primeiro segmento: "))
segundo_segmento = float(input("Digite o segundo segmento: "))
terceiro_segmento = float(input("Digite o terceiro segmento: "))

# Verifica a condição de existência de um triângulo
if primeiro_segmento + segundo_segmento > terceiro_segmento and primeiro_segmento + terceiro_segmento > segundo_segmento and segundo_segmento + terceiro_segmento > primeiro_segmento:
    print("As retas PODEM FORMAR um triângulo", end=' ')
    #EQUILATERO
    if primeiro_segmento == segundo_segmento and primeiro_segmento == terceiro_segmento:
        print("EQUILÁTERO")
    #ISÓCELES
    elif primeiro_segmento == segundo_segmento and primeiro_segmento != terceiro_segmento:
        print("ISÓCELES")
    #ESCALENO
    elif primeiro_segmento != segundo_segmento and primeiro_segmento != terceiro_segmento:
        print("ESCALENO")
else:
    print("As retas NÃO podem formar um triângulo.")