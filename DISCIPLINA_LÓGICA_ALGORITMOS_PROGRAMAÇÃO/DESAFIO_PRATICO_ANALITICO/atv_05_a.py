# 5. Observe o código a seguir e analise as questões pedidas

L = [15, 7, 27, 39]
p = int(input("Digite um valor a procurar: "))
achou = False 
x = 0
while x < len(L):
    if L[x] == p:
        achou = True 
        break
    x += 1
if achou: 
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")

# a) Explique a função das linhas 20, 24, 25 e 27

'''
LINHA 20 : SERVE PARA INDICAR SE O VALOR FOI ENCONTRADO OU NÃO, INICIALMENTE É FALSO, POIS AINDA NÃO FOI PROCURADO.
LINHA 24 : SERVE PARA INDICAR QUE O VALOR FOI ENCONTRADO, ENTÃO A VARIÁVEL achou É ALTERADA PARA true.
LINHA 25 : SERVE PARA INTERROMPER O LAÇO while, POIS O VALOR JÁ FOI ENCONTRADO, ENTÃO NÃO HÁ NECESSIDADE DE CONTINUAR A PROCURA.
LINHA 27 : VERIFICA SE O VALOR FOI ENCONTRADO OU NÃO, SE achou FOR true, SIGNIFICA QUE O VALOR FOI ENCONTRADO, ENTÃO IMPRIME A POSIÇÃO
ONDE FOI ENCONTRADO, CASO CONTRÁRIO, IMPRIME QUE O VALOR NÃO FOI ENCONTRADO.

'''

