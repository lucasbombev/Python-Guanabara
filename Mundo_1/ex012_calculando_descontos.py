#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input("Qual é o preço do produto? R$"))
desconto = preco * 0.95
print(f"O produto que custava R${preco} na promoção com deconto de 5% vai custar R${desconto:.2f}.")