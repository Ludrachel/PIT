'''Classificador de Triângulos. Peça ao usuário para digitar o comprimento de
três lados de um triângulo. Determine se os lados formam um triângulo válido
e, em caso afirmativo, classifique-o como Equilátero, Isósceles ou Escaleno.
Regras:
a) Para ser um triângulo, a soma de dois lados deve ser maior que o terceiro
lado (a + b > c, a + c > b, b + c > a).
b) Equilátero: Todos os três lados são iguais.
c) Isósceles: Dois lados são iguais.
d) Escaleno: Todos os três lados são diferentes. '''

a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c: 
        print("Triângulo Isóseles")
    else:
        print("Triângulo Escaleno")
else:
    print("forma de triângulo inválida")