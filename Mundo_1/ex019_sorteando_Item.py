# Importa a biblioteca random, que contém funções para operações aleatórias.
import random

# Recebe os nomes dos quatro alunos através do input do usuário e armazena-os nas variáveis aluno1, aluno2, aluno3, e aluno4.
aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")

# Cria uma lista 'todos_alunos' contendo os quatro alunos.
todos_alunos = [aluno1, aluno2, aluno3, aluno4]

# Seleciona aleatoriamente um aluno da lista 'todos_alunos' e armazena na variável aluno_aleatorio.
aluno_aleatorio = random.choice(todos_alunos)

# Exibe o nome do aluno escolhido aleatoriamente.
print(f"O aluno escolhido foi {aluno_aleatorio}")
