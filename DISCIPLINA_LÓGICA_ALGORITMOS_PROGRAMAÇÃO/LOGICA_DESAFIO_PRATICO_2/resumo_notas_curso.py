'''Resumo estatistico de notas de um curso. Leia as notas de uma turma ate que
o usuario digite algo para sair. Para cada nota valida, determine se o estudante
foi aprovado, ficou em recuperacao ou foi reprovado. Considere aprovado para
nota maior ou igual a 7,0, recuperacao para nota entre 5,0 e 6,9, e reprovacao
para nota inferior a 5,0.
Ao final, apresente a media da turma, a maior nota, a menor nota, o percentual
de aprovacao e a situacao geral da turma. Classifique a turma como “desempenho
satisfatorio” quando o percentual de aprovacao for igual ou superior a 70%.
Requisitos: utilizar while; aceitar notas entre 0 e 10; nao encerrar a leitura ao
receber um valor invalido; impedir divisao por zero; utilizar decisoes para a
situacao individual e para a classificacao geral. 
'''

soma = 0
quantidade = 0
aprovados = 0
maior = None
menor = None

while True:       # CONTINUA LENDO NOTAS ATÉ O USUÁRIO DIGITAR "SAIR"
    notas = input("DIGITE A NOTA (OU 'SAIR' PARA ENCERRAR): ")
    if notas.upper() == 'SAIR':
        break
    
    try:         # EVITA QUE O PROGRAMA DÊ ERRO CASO O USUÁRIO DIGITE LETRAS OU CARACTERES INVÁLIDOS
        notas = float(notas)
        if notas < 0 or notas > 10:  # NOTAS MENORES QUE 0 MAIORES QUE 10 SÃO CONSIDERADAS INVÁLIDAS
            print("NOTA INVÁLIDA!")  # MAS NÃO ENCERRAM O PROGRAMA
            continue
   
        if notas >= 7:
            print("APROVADO!")
            aprovados += 1
        elif notas >= 5:
            print("RECUPERAÇÃO")
        else:
            print("REPROVADO!")


        soma += notas
        quantidade += 1

        if maior is None or notas > maior:
            maior = notas
        if menor is None or notas < menor:
            menor = notas

    except ValueError:
        print("Entrada inválida! Digite uma nota ou 'SAIR'. ")

if quantidade > 0:               # IMPEDE A DIVISÃO POR ZERO
    media = soma / quantidade
    percentual_aprovacao = (aprovados / quantidade) * 100

    if percentual_aprovacao >= 70:
        situacao_geral = "DESEMPENHO SATISFATÓRIO"
    else:
        situacao_geral = "DESEMPENHO INSATISFATÓRIO"

    print("---RESULTADO DA TURMA---")
    print(f"MÉDIA DA TURMA: {media:.2f}")
    print(f"MAIOR NOTA: {maior:.2f}")
    print(f"MENOR NOTA: {menor:.2f}")
    print(f"PERCENTUAL DE APROVAÇÃO: {percentual_aprovacao:.2f}%")
    print(f"SITUAÇÃO GERAL: {situacao_geral}")

else:
    print("NENHUMA NOTA VÁLIDA FOI REGISTRADA.")