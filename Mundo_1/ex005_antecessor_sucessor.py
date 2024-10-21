#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
# Solicitar um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Calcular o sucessor e o antecessor
sucessor = numero + 1
antecessor = numero - 1

# Mostrar o sucessor e o antecessor na tela
print(f"O sucessor de {numero} é {sucessor} e o antecessor é {antecessor}.")
