#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# Importa a biblioteca random, que contém funções para operações aleatórias.
import random

# Recebe os nomes dos quatro alunos através do input do usuário e armazena-os nas variáveis aluno1, aluno2, aluno3, e aluno4.
aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")

# Cria uma lista 'todos_alunos' contendo os quatro alunos.
todos_alunos = [aluno1, aluno2, aluno3, aluno4]
#randomiza
random.shuffle(todos_alunos)
#mostra a ordem trocada
print(todos_alunos)