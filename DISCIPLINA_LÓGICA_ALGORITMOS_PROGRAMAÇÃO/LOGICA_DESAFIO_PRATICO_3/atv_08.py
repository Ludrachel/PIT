def verificar_senha(senha):
    return len(senha) >= 8


# Programa principal
senha = input("Digite uma senha: ")

if verificar_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida!")



# DESAFIO
def verificar_senha(senha):
    tem_numero = any(caractere.isdigit() for caractere in senha)

    return len(senha) >= 8 and tem_numero


# Programa principal
senha = input("Digite uma senha: ")

if verificar_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida!")