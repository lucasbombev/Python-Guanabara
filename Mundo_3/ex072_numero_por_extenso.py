# Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# O programa deve ler um número entre 0 e 20 e mostrar esse número por extenso.

# Tupla com os números de 0 a 20 escritos por extenso.
extensos = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
    'dezoito', 'dezenove', 'vinte'
)

# Laço infinito para garantir que o usuário digite um número válido
while True:
    numero = int(input("Digite um número entre 0 e 20: "))  # Lê o número do usuário
    if numero > 20 or numero < 0:  # Verifica se está fora da faixa permitida
        print("Tente novamente.")  # Informa que o número está inválido
    else:
        break  # Se o número estiver entre 0 e 20, sai do laço

# Mostra o número digitado por extenso, acessando o índice correspondente na tupla
print(f"Você digitou o número {extensos[numero]}")
