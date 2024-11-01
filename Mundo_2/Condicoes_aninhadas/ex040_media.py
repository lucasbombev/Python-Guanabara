'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO'''
nota_1 = float(input("Primeira nota: "))
nota_2 = float(input("Segunda nota: "))
media = (nota_1 + nota_2) / 2
print(f"Tirando {nota_1} e {nota_2}, a média do aluno é {media}")
if media >= 7:
    print("Aluno APROVADO, meus parabéns!")
elif media >= 5 and media < 7:
    print("Aluno de RECUPERAÇÃO, estude que ainda da tempo!")
else:
    print("Aluno REPROVADO, é muito ser burro kkkkkkk")