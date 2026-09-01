'''Seleção de atributos para um modelo. Um conjunto de dados possui n atributos
disponíveis. O analista deseja selecionar r atributos para uma etapa de
modelagem, sem considerar a ordem de seleção. Calcule o número de
subconjuntos possíveis usando: C(n, r) = n! / (r! * (n-r)!)
O programa deve validar 0 <= r <= n e informar se a quantidade de subconjuntos
é compatível com uma busca exaustiva. Considere viável a busca quando houver
até 10.000 combinações.
Requisitos: calcular o resultado sem função pronta de fatorial; utilizar repetição;
aplicar decisões para validar os parâmetros e classificar a viabilidade; explicar
por que a ordem dos atributos não altera uma combinação. '''

# Entrada de Dados
n = int(input("Digite a quantidade de atributos (n): "))
r = int(input("Digite quantos atributos deseja selecionar (r): "))

# Validação
if r < 0 or r > n:
    print("Valores inválidos! Deve ser 0 <= r <= n.")

else:
    # Calculando n!
    fatorial_n = 1                        # Inicializa a variável fatorial_n com 1
    for i in range(1, n + 1):             # Itera de 1 até n para calcular o fatorial de n
        fatorial_n = fatorial_n * i       # Multiplica o valor atual de fatorial_n pelo valor de i

    # Calculando r!
    fatorial_r = 1
    for i in range(1, r + 1):
        fatorial_r = fatorial_r * i

    # Calculando (n-r)!
    fatorial_nr = 1
    for i in range(1, n - r + 1):          # Itera de 1 até (n-r) para calcular o fatorial de (n-r)
        fatorial_nr = fatorial_nr * i      # Multiplica o valor atual de fatorial_nr pelo valor de i

    # Fórmula da combinação
    combinacoes = fatorial_n / (fatorial_r * fatorial_nr)

    print("Número de subconjuntos:", int(combinacoes))

    # Verificando se a busca é viável
    if combinacoes <= 10000:
        print("Busca exaustiva viável.")
    else:
        print("Busca exaustiva não viável.")

'''A ordem não altera a combinação porque escolher A, B e C representa o mesmo subconjunto
 que escolher C, B e A. A combinação conta apenas quais atributos foram escolhidos, e não a ordem
em que foram escolhidos.'''



