peso = int(input("Qual seu peso? (Kg): "))
altura = float(input("Qual sua altura? (m): "))
imc = peso / altura**2

print(f"IMC: {imc:.0f}")
if imc > 30:
    print("OBESO MONSTRO DEVORADOR!")
elif imc < 30 and imc > 25:
    print("SOBREPESO!")
elif imc < 25 and imc > 18.5:
    print("PESO NORMAL")
elif imc < 18.5:
    print("PASSANDO FOME!") 