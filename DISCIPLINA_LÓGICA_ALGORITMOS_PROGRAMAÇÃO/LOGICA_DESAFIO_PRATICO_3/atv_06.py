def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade


# Programa principal
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = calcular_idade(ano_nascimento, ano_atual)

print(f"Idade: {idade} anos")

if idade < 18:
    print("A pessoa é menor de idade.")
else:
    print("A pessoa é maior de idade.")