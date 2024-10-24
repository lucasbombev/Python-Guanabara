#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime

# Obter o ano atual
ano_atual = datetime.datetime.now().year

# Solicitar o ano de nascimento
nascimento = int(input("Ano de nascimento: "))

# Calcular a idade
idade = ano_atual - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.")

# Se passou do tempo de alistamento
if idade > 18:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.")
    print(f"Seu alistamento foi em: {nascimento + 18}")

# Se ainda não chegou o tempo de alistamento
elif idade < 18:
    print(f"Ainda faltam {18 - idade} anos para o alistamento.")
    print(f"Seu alistamento será em: {nascimento + 18}")

# Se é a hora exata de se alistar
else:
    print("Você deve se alistar IMEDIATAMENTE!")
