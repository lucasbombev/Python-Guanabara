#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celcius = float(input("Informe a temperatura em ºC: "))
fahrenheit = (9/5*celcius) + 32
print(f"A temperatura de {celcius:.1f}ºC corresponde a {fahrenheit:.1f}ºF!")
