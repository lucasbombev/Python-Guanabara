#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
print('''
      Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA
''')
escolhas_validas = [0,1,2]
player_choice = int(input("Qual é sua jogada? "))
if player_choice not in escolhas_validas:
      print("ESCOLHA INVÁLIDA!")
else:
      pc_choice = random.randint(0,2)
      #JOKENPO SLEEPER
      sleep(0.4)
      print("JO")
      sleep(0.4)
      print("KEN")
      sleep(0.4)
      print("PO!!!")
      print("-="*20)
      #COMPUTADOR PLAY
      print("Computador jogou ",end='')
      if pc_choice == 0:
            print("PEDRA")
      elif pc_choice == 1:
            print("PAPEL")
      elif pc_choice == 2:
            print("TESOURA")
      #PLAYER PLAY
      print("Jogador jogou ", end='')
      if player_choice == 0:
            print("PEDRA")
      elif player_choice == 1:
            print("PAPEL")
      elif player_choice == 2:
            print("TESOURA")
      print("-="*20)
      #TESTE JOGADOR VENCE
      if player_choice == 0 and pc_choice == 2:
            print("JOGADOR VENCE")
      elif player_choice == 1 and pc_choice == 0:
            print("JOGADOR VENCE")
      elif player_choice == 2 and pc_choice == 1:
            print("JOGADOR VENCE")
      #TESTE MAQUINA VENCE
      elif pc_choice == 0 and player_choice == 2:
            print("MAQUINA VENCE")
      elif pc_choice == 1 and player_choice == 0:
            print("MAQUINA VENCE")
      elif pc_choice == 2 and player_choice == 1:
            print("MAQUINA VENCE")
      else:
            print("EMPATE")