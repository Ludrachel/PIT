def area_triangulo(base, altura):
    return (base * altura) / 2


def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2


def area_losango(diagonal_maior, diagonal_menor):
    return (diagonal_maior * diagonal_menor) / 2


# Programa principal

# Triângulo
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
print(f"Área do triângulo: {area_triangulo(base, altura):.2f}")

# Trapézio
base_maior = float(input("\nDigite a base maior do trapézio: "))
base_menor = float(input("Digite a base menor do trapézio: "))
altura = float(input("Digite a altura do trapézio: "))
print(f"Área do trapézio: {area_trapezio(base_maior, base_menor, altura):.2f}")

# Losango
diagonal_maior = float(input("\nDigite a diagonal maior do losango: "))
diagonal_menor = float(input("Digite a diagonal menor do losango: "))
print(f"Área do losango: {area_losango(diagonal_maior, diagonal_menor):.2f}")