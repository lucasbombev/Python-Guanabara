dinheiro = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = dinheiro / 5.76
print(f"Com R${dinheiro:.2f} você pode comprar U${dolar:.2f}")
efe = input("press 'F' to respect!").upper().strip()
if efe == 'F':
    print("Obrigado pelo F!")