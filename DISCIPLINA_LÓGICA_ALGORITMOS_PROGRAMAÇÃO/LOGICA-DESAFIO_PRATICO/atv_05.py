'''Solicite os coeficientes a, b e c de uma equação do segundo grau (ax² + bx + c
= 0). Determine e mostre o número de raízes reais distintas que a equação
possui. Regra: O número de raízes reais depende do discriminante (delta),
Δ = b² - 4ac:
• Δ > 0: Duas raízes reais distintas.
• Δ = 0: Uma raiz real (ou duas raízes reais iguais).
• Δ < 0: Nenhuma raiz real (duas raízes complexas). '''

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta > 0:
    print("A equação possui duas raízes reais distintas.")
elif delta == 0:
    print("A equação possui uma raiz real.")
else:
    print("A equação não possui raízes reais.")