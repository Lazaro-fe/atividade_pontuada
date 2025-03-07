# LIMPEZA DO TERMINAL
import os
os.system("clear")

# sOLICITANDO DADOS AO USUÁRIO 

a = float(input("Digite o primeiro número : "))
b = float(input("Digite o segundo número : "))

opcao = int(input("Digite a opcao correspondente : "))

# PROCESSANDO

match opcao :
    case 1:
        if a == b:
       
         c = a+b
        print(f"A : {a}")
        print(f"B : {b}")
        print(f"C : {c}")
    case 2:
        if a != b:
         c = a * b
        print(f"A : {a}")
        print(f"B : {b}")
        print(f"C : {c}")
    case _:
        print("Opção inválida")