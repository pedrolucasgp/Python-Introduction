notaA = float(input("Informe a N1: "))
notaB = float(input("Informe a N2: "))

mediafinal = (notaA+notaB) / 2

if mediafinal >=7.00:
    print("Aprovado com média: %.1f"% mediafinal)
else:
    print("Reprovado com média: %.1f"% mediafinal)