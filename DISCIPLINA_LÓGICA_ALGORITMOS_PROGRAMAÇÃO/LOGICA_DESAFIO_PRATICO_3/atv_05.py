def calcular_estacionamento(tempo):
    if tempo <= 1:
        valor = 5.00
    elif tempo <= 3:
        valor = 10.00
    elif tempo <= 5:
        valor = 15.00
    else:
        valor = 20.00

    return valor


# Programa principal
tempo = float(input("Digite o tempo de permanência em horas: "))

valor_final = calcular_estacionamento(tempo)

print(f"Valor a pagar: R$ {valor_final:.2f}")