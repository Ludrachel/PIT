'''
3. Faça um programa que leia duas listas, A e B, e que gere uma terceira com os
elementos das duas primeiras.
A = ['mouse', 'teclado', 'monitor', 'estabilizador']
B = ['memória', 'cpu', 'ssd', 'chipset', 'rom'] 

'''

A = ['mouse', 'teclado', 'monitor', 'estabilizador']
B = ['memória', 'cpu', 'ssd', 'chipset', 'rom']
C = [] 

for elemento in A:
    C.append(elemento)
for elemento in B:
    C.append(elemento)
print(C)
