#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. 
from datetime import datetime
ano_atual = datetime.now().year
ano_nascimento = int(input("Ano de nascimento: "))
idade = ano_atual - ano_nascimento
print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.")

if idade == 18:
    print("Este é o ano que você deve se alistar! CORRE BISONHO")
elif idade <= 18:
    print(f"Ainda faltam {18 - idade} anos para o alistamento")
    print(f"Seu alistamento será em {ano_nascimento + 18}.")
else:
    print(f"você já devia ter se alistado há {idade - 18} anos.")
    