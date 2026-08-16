'''Verificador de Par ou Ímpar. Peça ao usuário um número inteiro e diga se ele
é par ou ímpar. '''

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
