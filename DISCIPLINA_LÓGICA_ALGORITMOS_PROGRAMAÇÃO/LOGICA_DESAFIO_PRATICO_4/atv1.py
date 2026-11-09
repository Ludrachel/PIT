import random


def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    palpites = []

    print("=== Jogo de Adivinhação ===")
    print("Pensei em um número de 1 a 100. Tente adivinhar!")

    while True:
        palpite = int(input("Digite seu palpite: "))
        palpites.append(palpite)

        if palpite == numero_secreto:
            print("\nParabéns, você acertou!")
            print("Números digitados:", palpites)
            print("Quantidade de tentativas:", len(palpites))
            break
        elif numero_secreto > palpite:
            print("Errou! Dica: o número é MAIOR que", palpite)
        else:
            print("Errou! Dica: o número é MENOR que", palpite)


jogo_adivinhacao()
