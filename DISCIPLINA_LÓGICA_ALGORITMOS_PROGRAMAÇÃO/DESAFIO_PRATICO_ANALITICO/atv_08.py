'''
8. Escreva um código que receba números ou palavras. O código deve
armazenar cada situação em listas diferentes, ou seja, uma lista só para as
palavras e outra só para os números. O programa deve encerrar quando o
usuário digitar o x ou X. No fim, mostre o que foi inserido nas duas listas, a
quantidade total de coisas digitadas pelo usuário. (Dica: métodos em Python) 
'''

numeros = []
palavras = []
while True:
    entrada = input("Digite um número ou uma palavra, ou 'x' para sair: ")
    if entrada.lower() == 'x':   # encerra o loop se o usuário digitar 'x' ou 'X'
      break
    elif entrada.lstrip('-').isdigit():  # verifica se a entrada é um número (considerando números negativos) 
        numeros.append(int(entrada))
    else:
        palavras.append(entrada)

print(f"Lista de números: {numeros}")
print(f"Lista de palavras: {palavras}")
print(f"Total digitado: {len(numeros) + len(palavras)} coisas.")