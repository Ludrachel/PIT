'''1.Observe o código apresentado a seguir e veja outras formas de inserir dados
em uma lista. '''

'''
numeros = [0,0,0,0,0]
x = 0
while x < 5:
    numeros[x] = float(input('DIGITE UM NÚMERO QUALQUER: '))
    x += 1
y = 0
while y < 5:
    print(f"{numeros[y]}")
    y += 1   
'''

# a) Refaça o código utilizando a estrutura FOR 

numeros = [0,0,0,0,0]
for x in range(5):
    numeros[x] = float(input('Digite um número qualquer: '))
for y in range(5):
    print(f"{numeros[y]}")