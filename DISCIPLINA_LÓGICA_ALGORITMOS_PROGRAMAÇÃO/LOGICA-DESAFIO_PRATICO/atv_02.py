'''Classificador de Idade. Solicite a idade de uma pessoa. Classifique-a como
"Criança" (0-12 anos), "Adolescente" (13-17 anos), "Adulto" (18-64 anos) ou "Idoso"
(65 anos ou mais). 
'''

idade = int(input("Digite a idade da pessoa: "))

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 64:
    print("Adulto")
else:
    print("Idoso")