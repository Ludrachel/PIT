# b) O que acontece se colocarmos while <= 4: ? Justifique.

numeros = [0,0,0,0,0]
x = 0
while x <= 4:
    numeros[x] = float(input('DIGITE UM NÚMERO QUALQUER: '))
    x += 1
y = 0
while y <= 4:
    print(f"{numeros[y]}")
    y += 1  

'''NADA MUDA NO RESULTADO, POIS O INTERVALO DE 0 A 4 É O MESMO QUE O INTERVALO DE 0 A 5, OU
SEJA AS DUAS CONDIÇÕES FAZEM O WHILE SE REPETIR 5 VEZES.'''

