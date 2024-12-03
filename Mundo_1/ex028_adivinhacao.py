
#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
# Adicionando cores ao programa usando ANSI Escape Codes
cores = {
    'vermelho': '\033[31m',  # Texto em vermelho
    'verde': '\033[32m',     # Texto em verde
    'amarelo': '\033[33m',   # Texto em amarelo
    'azul': '\033[34m',      # Texto em azul
    'magenta': '\033[35m',   # Texto em magenta
    'ciano': '\033[36m',     # Texto em ciano
    'limpa': '\033[m'        # Reseta a cor para padrão
}

# Introdução do programa com cores
print(cores['azul'] + 20 * "-=" + cores['limpa'])
print(cores['ciano'] + "Vou pensar em um número entre 0 e 5. Tente adivinhar..." + cores['limpa'])
print(cores['azul'] + 20 * "-=" + cores['limpa'])

# Entrada do usuário
numero = int(input(cores['amarelo'] + "Em que número eu pensei? " + cores['limpa']))

# Computador "pensa" em um número aleatório entre 0 e 5
pc_numero = random.randint(0, 5)

# Simula processamento com uma pausa
print(cores['magenta'] + "PROCESSANDO..." + cores['limpa'])
time.sleep(1.5)

# Verifica se o número escolhido pelo usuário é igual ao do computador
if numero == pc_numero:
    # Mensagem de vitória
    print(cores['verde'] + f"PARABÉNS! Eu realmente pensei no número {numero}. Você venceu!" + cores['limpa'])
else:
    # Mensagem de derrota
    print(cores['vermelho'] + f"GANHEI! Eu pensei no número {pc_numero}, não no {numero}!" + cores['limpa'])
