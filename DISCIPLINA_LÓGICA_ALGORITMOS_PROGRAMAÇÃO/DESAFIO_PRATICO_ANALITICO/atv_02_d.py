# d) Reescreva o código para que o mesmo possa funcionar para qualquer lista L 

L = [1,2,3,4,5,6,7,8,9]
x = 0
while x < len(L):
    print(L[x])
    x += 1

''' O USO DO len(L) PERMITE QUE O CÓDIGO FUNCIONE PARA QUALQUER LISTA, POIS O TAMANHO 
DA LISTA É CALCULADO AUTOMATICAMENTE.'''