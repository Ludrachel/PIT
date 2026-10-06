''' 7. Sabemos que as listas possuem funções que ajudam a construir programas
 sem escrever muito código. Vimos as funções: max(), min(), sum() e enumerate(). 
'''

'''
T = [-10, -8, 0, 1, 2, 20, -2, -4]
soma = 0
for i in range(len(T)):
    soma += T[i]
print(f"A soma total da lista é: {soma}")

'''

# O código acima faz a soma de todos os números da lista sem utilizar a funçãosum(). Utilizando o código como base, faça: 
# a) Um código para descobrir o maior número da lista 

T = [-10, -8, 0, 1, 2, 20, -2, -4]
maior = T[0]   # inicializa a variável maior com o primeiro elemento da lista
for i in range(len(T)):
    if T[i] > maior:
        maior = T[i]
print(f"O maior número da lista é: {maior}")