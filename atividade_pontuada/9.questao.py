# Limpeza do Terminal
import os
os.system("clear")

# Solicitando dados ao Usuário

valor_da_renda_mensal = float(input("Digite sua renda mensal : "))
valor_do_emprestimo = float(input("Digite o valor do emprestimo que você quer : "))

prestações = valor_da_renda_mensal * 0.3

# Processamento

if valor_da_renda_mensal * 10 >= valor_do_emprestimo:
    prestações =  valor_da_renda_mensal * 0.3
    print("Emprestimo Válidado")
elif valor_da_renda_mensal * 10 != valor_do_emprestimo :
    print("Emprestimo inválidado")
else :
    print("Emprestimo inválidado")


# Exibindo Resultados

print()
print(f"Valor da renda ganha mensalmente : {valor_da_renda_mensal}")
print(f"Valor do empréstimo solicitado : {valor_do_emprestimo}")
print(f"Valor da prestações a serem pagas : {prestações}")