# Limpeza do Terminal
import os
os.system("clear")

# Solicitando dados ao Usuário

print("""

========================== TABELA DE PREÇOS ==========================

    \tCOR                   \tPREÇO

    \tVerde                 \t10.00
    \tAzul                  \t20.00
    \tAmarelo               \t30.00
    \tVermelho              \t40.00

""")

cores = input("Digite a cor correspondente ao CD desejado : ")

# Verificando

match cores:
    case "Verde":
        cor_do_cd = "Verde"
        valor = 10.00
    case "Azul":
        cor_do_cd = "Azul"
        valor = 20.00
    case "Amarelo":
        cor_do_cd = "Amarelo"
        valor = 30.00
    case "Vermelho":
        cor_do_cd = "Vermelho"
        valor = 40.00
    case _:
        cor_do_cd = "Inváilido"
        valor = 0

# Exibindo Resultados

print()
print(f"CD escolhido foi : {cor_do_cd}")
print(f"Valor : {valor}")