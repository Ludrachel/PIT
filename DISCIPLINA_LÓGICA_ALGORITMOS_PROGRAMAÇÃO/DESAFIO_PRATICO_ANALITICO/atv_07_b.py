# b) Um código para descobrir o menor número da lista

T = [-10, -8, 0, 1, 2, 20, -2, -4]
menor = T[0]   # inicializa a variável menor com o primeiro elemento da lista
for i in range(len(T)):
    if T[i] < menor:
        menor = T[i]
print(f"O menor número da lista é: {menor}")