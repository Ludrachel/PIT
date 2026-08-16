'''Mini Calculadora. Crie uma mini calculadora que permita ao usuário escolher
entre as operações de soma, subtração, multiplicação e divisão. Peça dois
números e a operação desejada. Imprima o resultado. '''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação ( + (soma), - (subtração), * (multiplicação) ou / (divisão)): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Não é possível dividir por zero."
else:
    resultado = "Operação inválida."

print("Resultado:", resultado)