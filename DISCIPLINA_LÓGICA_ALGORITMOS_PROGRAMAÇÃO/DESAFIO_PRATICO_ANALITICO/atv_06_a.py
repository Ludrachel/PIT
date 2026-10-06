# 6. Observe o código a seguir e analise as questões pedidas

'''
L = []
while True:
    n = int(input("Digite um número ou 0 para sair: "))
    if n == 0:
        break
    L.append(n)

x = 0
while x < len(L):
    print(L[x])
    x = x + 1

'''

# a) Modifique o código usando a estrutura FOR para as duas repetições. 

L = []
for i in range(1000):  # limite arbitrário para evitar loop infinito
    n = int(input("Digite um número ou 0 para sair: "))
    if n == 0:
        break
    L.append(n)

for x in range(len(L)):
    print(L[x])