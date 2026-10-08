# 1. Faça um programa em Python que receba 10 idades, calcule e exiba:
# a) a média das idades.
# b) a mediana;
# c) a moda.


idades = []

# Receber 10 idades
for i in range(10):               
    idade = int(input(f"Digite a {i + 1}ª idade: "))
    idades.append(idade)

# a) Média
soma = 0

for idade in idades:
    soma += idade

media = soma / 10

# Ordenar as idades
idades.sort()

# b) Mediana
mediana = (idades[4] + idades[5]) / 2

# c) Moda
maior_frequencia = 0
moda = idades[0]

for idade in idades:
    frequencia = idades.count(idade)

    if frequencia > maior_frequencia:
        maior_frequencia = frequencia
        moda = idade

# Exibir resultados
print("\nResultados:")
print("Média:", media)
print("Mediana:", mediana)
print("Moda:", moda)