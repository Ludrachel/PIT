'''Utilizando uma estrutura de repetição, escreva um programa em Python que
calcule o fatorial de um número informado pelo usuário. '''

# Solicitando ao usuário que informe um número inteiro
numero = int(input("Digite um número inteiro para calcular o seu fatorial: "))

# Inicializando a variável fatorial com 1
fatorial = 1

# Utilizando uma estrutura de repetição para calcular o fatorial
for i in range(1, numero + 1):   # Itera de 1 até o número informado pelo usuário
    fatorial = fatorial * i      # Multiplica o valor atual de fatorial pelo valor de i

# Exibe o resultado
print(f"O fatorial de {numero} é: {fatorial}")
