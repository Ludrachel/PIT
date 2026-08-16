'''Ajude um hotel da cidade a calcular o valor da hospedagem. O hotel cobra R$
290,00 a diária e mais uma taxa de serviços. A taxa de serviços é de:
• R$ 6,50 por dia, se o número de diárias for maior que 7;
• R$ 12,00 por dia, se o número de diárias for igual a 7;
• R$ 16,50 por diária, se o número de diárias for menor que 7.
Você deve pedir a informação de quantos dias o hóspede ficou hospedado.
Construa um código que mostre o nome do hóspede e o total da conta a pagar. '''

nome = input("Digite o nome do hóspede: ")
dias = int(input("Digite a quantidade de dias hospedado: "))
diaria = 290.00

if dias > 7:
    taxa = 6.50
elif dias == 7:
    taxa = 12.00
else:
    taxa = 16.50

total = (diaria + taxa) * dias

print("\n--- CONTA DO HÓSPEDE ---")
print("Nome:", nome)
print(f"Total da conta: R$ {total:.2f}")

