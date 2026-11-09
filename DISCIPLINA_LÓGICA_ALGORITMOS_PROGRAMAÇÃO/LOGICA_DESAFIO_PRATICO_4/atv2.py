import math


def area_triangulo(b, h):
    return (b * h) / 2


def area_retangulo(b, h):
    return b * h


def area_quadrado(l):
    return math.pow(l, 2)


def area_trapezio(B, b, h):
    return ((B + b) * h) / 2


def area_losango(D, d):
    return (D * d) / 2


def area_circulo(r):
    return math.pi * math.pow(r, 2)


def menu():
    while True:
        print("\n=== Calculadora de Áreas ===")
        print("1 - Triângulo")
        print("2 - Retângulo")
        print("3 - Quadrado")
        print("4 - Trapézio")
        print("5 - Losango")
        print("6 - Círculo")
        print("0 - Sair")
        opcao = input("Escolha a figura: ")

        if opcao == "1":
            b = float(input("Base: "))
            h = float(input("Altura: "))
            print(f"Área do triângulo: {area_triangulo(b, h):.2f}")
        elif opcao == "2":
            b = float(input("Base: "))
            h = float(input("Altura: "))
            print(f"Área do retângulo: {area_retangulo(b, h):.2f}")
        elif opcao == "3":
            l = float(input("Lado: "))
            print(f"Área do quadrado: {area_quadrado(l):.2f}")
        elif opcao == "4":
            B = float(input("Base maior: "))
            b = float(input("Base menor: "))
            h = float(input("Altura: "))
            print(f"Área do trapézio: {area_trapezio(B, b, h):.2f}")
        elif opcao == "5":
            D = float(input("Diagonal maior: "))
            d = float(input("Diagonal menor: "))
            print(f"Área do losango: {area_losango(D, d):.2f}")
        elif opcao == "6":
            r = float(input("Raio: "))
            print(f"Área do círculo: {area_circulo(r):.2f}")
        elif opcao == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.")


menu()
