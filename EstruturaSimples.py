A = input("Informe um valor para A: ")
B = input("Informe um valor para B: ")

if (A>B):
    aux=A;
    A=B;
    B=aux;
print("O valor ce A agora é: ", A)
print("O valor de B agora é: ", B)