'''Uma empresa de vendas possui corretores. A empresa paga ao corretor uma
comissão calculada de acordo com o valor de suas vendas. Se o valor da venda
de um corretor for até R$ 500.000 a comissão será de 6% do valor vendido. Se o
valor da venda do corretor estiver acima de R$ 500.000 até R$ 700.000 a
comissão será de 8.5%. Se o valor da venda do corretor estiver acima de R$
700.000 até R$ 1.000.000 a comissão será de 10%. Se o valor da venda de um
corretor for maior que R$ 1.000.000 a comissão será de 12% do valor vendido.
Escreva um código que imprima um relatório contendo o nome, valor da venda
e a comissão do corretor. 
'''

nome = input("Digite o nome do corretor: ")
venda = float(input("Digite o valor da venda: R$ "))

if venda <= 500000:
    comissao = venda * 0.06
elif venda <= 700000:
    comissao = venda * 0.085
elif venda <= 1000000:
    comissao = venda * 0.10
else:
    comissao = venda * 0.12

print("\n--- RELATÓRIO ---")
print("Nome:", nome)
print(f"Valor da venda: R$ {venda:.2f}")
print(f"Comissão: R$ {comissao:.2f}")




