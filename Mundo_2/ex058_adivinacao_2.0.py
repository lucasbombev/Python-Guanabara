#IA generativa foi usada apenas para comentar o código.
# Jogo de Adivinhação: O computador escolhe um número e o usuário tenta acertar.
# Importa a função para gerar números aleatórios
from random import randint

# Gera um número aleatório entre 0 e 10
numero = randint(0, 10)

# Inicializa o contador de tentativas
contador_tentativas = 0

# Inicializa a variável 'palpite' com um valor fora do intervalo possível (para entrar no loop)
palpite = 999

# Mensagem inicial do jogo
print("Acabei de pensar em um número entre 0 e 10.")
print("Você consegue adivinhar qual foi?")

# Loop principal: repete enquanto o palpite estiver errado
while palpite != numero:
    # Pede o palpite do usuário e converte para número inteiro
    palpite = int(input("Qual o seu palpite? "))
    
    # Incrementa o contador de tentativas a cada palpite
    contador_tentativas += 1
    
    # Dá dicas ao usuário
    if palpite > numero:
        print("Menos... Tente mais uma vez.")
    elif palpite < numero:
        print("Mais... Tente mais uma vez.")

# Mensagem final quando o usuário acerta
print(f"Acertou na {contador_tentativas}ª tentativa. Parabéns!")