# c) O que aconteceria se atualizarmos a lista para L=[7,8,9,10,11,12]? Justifique 

L = [7,8,9,10,11,12]
x = 0
while x < 3:
    print(L[x])
    x += 1

''' O PROGRAMA IMPRIMIRÁ SOMENTE 7,8 E 9. A LISTA POSSUI 6 ELEMENTOS, MAS O CÓDIGO CONTINUA A IMPRIMIR SOMENTE OS 3 PRIMEIROS 
POR CAUSA DA CONDIÇÃO x < 3 QUE LIMITA O while A TRÊS REPETIÇÕES..'''