# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

import random

# Exibe as mensagens iniciais do jogo
print("=-"*10)
print("JOGO DO PAR OU IMPAR")
print("=-"*10)

# Define o número aleatório gerado pelo computador
computador = random.randint(1, 10)

# Variável para armazenar o cálculo de par ou ímpar
calcula_par_impar = 0
# Contador de vitórias consecutivas do jogador
conta_vitorias = 0

# Loop principal do jogo
while True:
    # Solicita ao jogador que insira um número
    player_number = int(input("Diga um valor:  "))
    # Solicita ao jogador que escolha entre Par ou Ímpar
    player_option = input("Par ou Ímpar? [P/I] ").upper()
    
    # Calcula se a soma dos números é par ou ímpar
    calcula_par_impar = (player_number + computador) % 2
    
    # Verifica se o jogador perdeu
    if player_option == 'P' and calcula_par_impar != 0:
        break

    # Incrementa o contador de vitórias consecutivas
    conta_vitorias += 1
    
    # Exibe o resultado da rodada
    print('-'*10)
    print(f"Você jogou {player_number} e o computador {computador}. Total de {player_number + computador}")

# Exibe a mensagem de fim de jogo e o total de vitórias consecutivas
print("=-"*10)
print(f"GAME OVER! Você venceu {conta_vitorias} vezes.")