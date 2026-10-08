'''
2. Uma caixa contém:
bolas = ["vermelha", "azul", "verde", "vermelha", "amarela", "azul", “vermelha",
"verde", "azul", "vermelha"]

Considerando que uma bola será escolhida ao acaso, crie um programa que:

a) conte quantas bolas existem na caixa;
b) conte quantas são vermelhas;
c) calcule a probabilidade de escolher uma bola vermelha;
d) apresente a probabilidade em forma de fração e porcentagem

'''
bolas = ["vermelha", "azul", "verde", "vermelha", "amarela",
         "azul", "vermelha", "verde", "azul", "vermelha"]

# a) Quantidade de bolas
quantidade = len(bolas)

# b) Quantidade de bolas vermelhas
vermelhas = bolas.count("vermelha")

# c) Probabilidade de escolher uma bola vermelha
probabilidade = vermelhas / quantidade

# d) Fração e porcentagem
fracao = f"{vermelhas}/{quantidade}"
porcentagem = probabilidade * 100

print("Quantidade de bolas:", quantidade)
print("Quantidade de bolas vermelhas:", vermelhas)
print("Probabilidade:", probabilidade)
print("Probabilidade em fração:", fracao)
print("Probabilidade em porcentagem:", porcentagem, "%")