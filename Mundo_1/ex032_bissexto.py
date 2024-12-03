#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import datetime
ano_atual = datetime.now().year
bissexto = int(input("Que ano quer analisar? Digite 0 para analisar o ano atual: "))
if bissexto == 0:
    bissexto = ano_atual
if (bissexto % 4 == 0) and ((bissexto % 100 != 0 ) or (bissexto % 400 == 0)):
    print(f"O ano {bissexto} é BISSEXTO")
else:
    print(f"O ano {bissexto} NÃO é BISSEXTO")
    