'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JÚNIOR
Até 25 anos: ADULTO
Acima de 25 anos: MASTER'''
from datetime import datetime
ano_atual = datetime.now().year
ano_nascimento = int(input("Ano de nascimento: "))
idade = ano_atual - ano_nascimento

print(f"O atleta tem {idade} anos.")
print("Classificação:  ",end='')

if idade < 9:
    print("MIRIM")
elif idade > 9 and idade <= 14:
    print("INFANTIL")
elif idade > 14 and idade <= 19:
    print("JÚNIOR")
elif idade > 19 and idade <= 25:
    print("ADULTO")
else:
    print("MASTER")