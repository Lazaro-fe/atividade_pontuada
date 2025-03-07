# Limpeza de Terminal
import os
os.system("clear")

# Solicitando dados ao Usuário

A = float(input("Digite o primeiro número : "))
B = float(input("Digite o segundo número : "))
C = float(input("Digite o terceiro número : "))
soma = A + B

# Solicitando dados ao Usuário

print()
if A + B < C:
    print(f"A soma {A} + {B} é menor que {C}")
elif A + B > C :
    print(f"Soma de {A} + {B} é maior que {C}")

# Exibindo os resultados 

print()
print(f"Primeiro número : {A}")
print(f"Segundo número : {B}")
print(f"Terceiro número : {C}")
print(f"Soma : {soma}")