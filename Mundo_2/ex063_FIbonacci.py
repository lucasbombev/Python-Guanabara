linha = '=' * 30
print(linha,"Sequência de Fibonacci",linha)
termos = int(input("Quantos termos você quer mostrar? "))
print(linha)
t1 = 0
t2 = 1
contador = 3
print(f"{t1} -> {t2}", end='')
while contador <= termos:
    t3 = t1 + t2
    print(f" -> {t3}", end='')
    t1 = t2
    t2 = t3
    contador+=1
print(" -> FIM")