#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maior = 0
menor = 0
ano_nascimento = 0
ano_atual = 2025 
for c in range(1,8):
    ano_nascimento = int(input(f"Em que ano a {c}ª pessoa nasceu?"))
    if ano_atual - ano_nascimento > 18:
        maior+=1
    else:
        menor+=1
print(f"Ao todo tivemos {maior} pessoas maiores de idade")
print(f"E também tivemos {menor} pessoas menores de idade")