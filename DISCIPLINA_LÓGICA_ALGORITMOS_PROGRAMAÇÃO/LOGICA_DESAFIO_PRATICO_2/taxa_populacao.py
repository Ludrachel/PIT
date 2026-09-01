'''Supondo que a população de um país A seja da ordem de 90.000 habitantes
com uma taxa anual de crescimento de 5% e que a população de B seja 200.000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. '''

# Inicializando as populações e taxas de crescimento
populacao_A = 90000
populacao_B = 200000
taxa_crescimento_A = 0.05 # 5%
taxa_crescimento_B = 0.015 # 1.5%
anos = 0

# Utilizando uma estrutura de repetição para calcular o número de anos necessários
while populacao_A < populacao_B:
    populacao_A += populacao_A * taxa_crescimento_A # Atualiza a população de A com base na taxa de crescimento
    populacao_B += populacao_B * taxa_crescimento_B # Atualiza a população de B
    anos += 1   # Incrementa o contador de anos

# Exibindo o resultado
print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B. ")

