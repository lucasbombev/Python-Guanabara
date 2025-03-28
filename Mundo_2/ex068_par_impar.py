#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
import random
print("=-"*10) 
print("JOGO DO PAR OU IMPAR")
print("=-"*10) 

computador = random.randint(1, 10)
calcula_par_impar = 0
conta_vitorias = 0

while True:
    player_number = int(input("Diga um valor:  "))
    player_option = input("Par ou Ímpar? [P/I] ").upper()
    calcula_par_impar = (player_number + computador) % 2
    if player_option == 'P' and calcula_par_impar != 0:
        break
    conta_vitorias += 1
    print('-'*10)
    print(f"você jogou {player_number} e o computador {computador}. Total de {player_number + computador}")
    print('-'*10)
print("=-"*10)    
print(f"GAME OVER! você venceu {conta_vitorias} vezes.")