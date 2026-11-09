import re


def verificar_senha(senha):
    erros = []

    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")
    if not re.search(r"[A-Z]", senha):
        erros.append("A senha deve conter pelo menos uma letra maiúscula.")
    if not re.search(r"[0-9]", senha):
        erros.append("A senha deve conter pelo menos um número.")

    return erros
from verificador_senha import verificar_senha

print("=== Verificador de Senhas ===")
senha = input("Digite a senha: ")

erros = verificar_senha(senha)

if len(erros) == 0:
    print("Senha válida! Ela está no padrão da empresa.")
else:
    print("Senha fora do padrão da empresa:")
    for erro in erros:
        print("-", erro)
