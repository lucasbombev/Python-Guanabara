#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
import random
# Imprime a introdução do jogo
print("=-"*10) 
print("JOGO DO PAR OU IMPAR")
print("=-"*10) 
# Gera um número aleatório entre 1 e 10 para o computador
computador = random.randint(1, 10)
# Inicializa as variáveis
calcula_par_impar = 0
conta_vitorias = 0
# Loop principal do jogo
while True:
    # Recebe o valor do jogador
    player_number = int(input("Diga um valor:  "))
    # Recebe a escolha do jogador (Par ou Ímpar) e converte para maiúsculas
    player_option = input("Par ou Ímpar? [P/I] ").upper()
    # Calcula se a soma é par ou ímpar
    calcula_par_impar = (player_number + computador) % 2
    # Verifica se o jogador escolheu Par e a soma é ímpar, então o jogo termina
    if player_option == 'P' and calcula_par_impar != 0:
        break
    # Incrementa o contador de vitórias
    conta_vitorias += 1
    # Imprime o resultado da rodada
    print('-'*10)
    print(f"Você jogou {player_number} e o computador {computador 