#Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
extensos = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    numero = int(input("Digite um número entre 0 e 20:"))
    if numero > 20 or numero < 0:
        print("Tente novamente.")
    else:
        break
print(f"Você digitou o número {extensos[numero]}")