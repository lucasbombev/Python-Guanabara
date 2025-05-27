#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
print("-"*20)
print("LISTAGEM DE PREÇOS")
print("-"*20)

produtos = (
str("Lápis.................R$  1.75\n"),
str("Borracha..............R$  2.00\n"),
str("Caderno...............R$  15.90\n"),
str("Estojo................R$  25.00\n"),
str("Transferidor..........R$  4.20\n"),
str("Compasso..............R$  9.99\n"),
str("Mochila...............R$  120.32\n"),
str("Canetas...............R$  22.30\n"),
str("Livros................R$  34.90\n"),
)
for c in produtos:
    print(c)