def lernotas():
    n=float(input("Digite a nota do aluno: "))
    return n

def calcularmedia(n1,n2):
    media = (n1+n2) / 2
    print("N1: ", n1)
    print("N2: ", n2)
    print("Media: ", media, "Resultado: ", end="")
    if media > 7:
        print("Aprovado")
    else:
        print("Reprovado")

a = lernotas()
b = lernotas()
calcularmedia(a, b)
