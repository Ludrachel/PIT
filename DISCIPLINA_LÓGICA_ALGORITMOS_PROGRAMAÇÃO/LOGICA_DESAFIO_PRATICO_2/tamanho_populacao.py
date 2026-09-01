'''Uma população inicial de 2727 indivíduos cresce a uma taxa de 4% ao ano.
Escreva um programa em Python que simule o crescimento dessa população e
mostre o tamanho da população ao final de cada ano, durante 5 anos. '''

# Inicializando a população e a taxa de crescimento
populacao = 2727
taxa_crescimento = 0.04 # 4%
anos = 5

# Utilizando uma estrutura de repetição para calcular o tamanho da população ao final de cada ano
for ano in range(1, anos + 1):
    populacao += populacao * taxa_crescimento  # Atualiza a população com base na taxa de crescimento
    print(f"A população ao final do ano {ano} será de: {int(populacao)} indivíduos. ")