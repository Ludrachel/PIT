import math


def calcular_raizes(a, b, c):
    delta = math.pow(b, 2) - 4 * a * c
    print(f"Delta = {delta}")

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A equação possui 2 raízes reais distintas.")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / (2 * a)
        print("A equação possui 1 raiz real (duas raízes reais iguais).")
        print(f"x = {x:.2f}")
    else:
        print("A equação não possui raízes reais (duas raízes complexas).")


print("=== Equação do 2º grau: ax² + bx + c = 0 ===")
a = float(input("Digite o valor de a: "))
while a == 0:
    print("O valor de 'a' não pode ser 0 em uma equação do 2º grau.")
    a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

calcular_raizes(a, b, c)
