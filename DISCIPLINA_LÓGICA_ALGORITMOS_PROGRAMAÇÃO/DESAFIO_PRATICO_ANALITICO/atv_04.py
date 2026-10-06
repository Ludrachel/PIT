'''
4. Faça um programa que percorra duas listas, A e B, e gere uma terceira sem
elementos repetidos.
A = ['Python', 'Java', 'C', 'PHP', 'JavaScript', 'Dart']
B = ['C++', 'Python', 'Java', 'Julia', 'Go', 'JavaScript'] 

'''

A = ['Python', 'Java', 'C', 'PHP', 'JavaScript', 'Dart']
B = ['C++', 'Python', 'Java', 'Julia', 'Go', 'JavaScript']
C = []

for elemento in A:
    if elemento not in C:
        C.append(elemento)
for elemento in B:
    if elemento not in C:
        C.append(elemento)

print(C)