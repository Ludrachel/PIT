alunos = [
    ["Ana", 7.5, 8.0, 9.0],
    ["Bruno", 6.0, 5.5, 7.0],
    ["Carlos", 9.0, 8.5, 10.0],
    ["Daniela", 5.0, 6.0, 4.5],
    ["Eduardo", 8.0, 7.5, 6.5]
]

soma_medias = 0
maior_media = 0
menor_media = 10
aluno_maior_media = ""
aluno_menor_media = ""
aprovados = 0
reprovados = 0

print("RELATÓRIO DOS ALUNOS")
print("--------------------")

for aluno in alunos:
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]
    nota3 = aluno[3]

    media = (nota1 + nota2 + nota3) / 3

    soma_medias += media

    if media >= 7:
        situacao = "Aprovado"
        aprovados += 1
    else:
        situacao = "Reprovado"
        reprovados += 1

    if media > maior_media:
        maior_media = media
        aluno_maior_media = nome

    if media < menor_media:
        menor_media = media
        aluno_menor_media = nome

    print(f"Aluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print()

# Média geral da turma
media_geral = soma_medias / len(alunos)

print("RESULTADO FINAL")
print("----------------")
print(f"Média geral da turma: {media_geral:.2f}")
print(f"Maior média: {aluno_maior_media} ({maior_media:.2f})")
print(f"Menor média: {aluno_menor_media} ({menor_media:.2f})")
print(f"Quantidade de aprovados: {aprovados}")
print(f"Quantidade de reprovados: {reprovados}")