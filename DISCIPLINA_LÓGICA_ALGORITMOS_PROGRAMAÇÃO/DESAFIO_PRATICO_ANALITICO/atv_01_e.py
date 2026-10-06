# e) Refaça o código melhorando os problemas encontrados na alternativa (c e d)

numeros = []
quantidade = int(input("Quantos números você deseja inserir? "))
for x in range(quantidade):
    numero = float(input("Digite um número: "))
    numeros.append(numero)
for numero in numeros:
    print(numero)