#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = int(input("Digite uma distância em metros: "))
centimetros = metros * 100
milimetros = metros * 1000
print(f"A medida de {metros}m corresponde a")
print(f"{centimetros}cm")
print(f"{milimetros}mm")