'''Probabilidade experimental. Um experimento consiste em lançar um dado 20
vezes. O programa recebe o resultado de cada lançamento e deve contar quantas
vezes apareceu um número par. Ao final, deve calcular a probabilidade
experimental de obter um número par'''

# Inicializando a contagem de números pares
contagem_pares = 0

# Solicitando ao usuário que informe o resultado de cada lançamento do dado
for i in range(1, 21):                             # Itera de 1 até 20 
    resultado = int(input(f"Digite o resultado do lançamento {i} (1 a 6): "))
    if resultado < 1 or resultado > 6:             # Valida se o resultado está entre 1 e 6
        print("Resultado inválido! Digite um número entre 1 e 6.")
        continue                                   # Pula para a próxima iteração do loop se o resultado for inválido
    if resultado % 2 == 0:                         # Verifica se o resultado é par
        contagem_pares += 1                        # Incrementa a contagem de números pares

# Calculando a probabilidade experimental de obter um número par
prob_experimental = contagem_pares / 20           
print(f"A probabilidade experimental de obter um número par é: {prob_experimental:.2f}")