#   Limpando o Terminal
import os
os.system("clear")

#   Solicitando dados ao usuário

A = int(input("Digite o primeiro número : "))
B = int(input("Digite o segundo número : "))
operacao = input("Digite a operação desejada : ")

#   Verificando

match operacao:
    case"+":
        resultado = A + B
    case"-":
        resultado = A - B
    case"*":
        resultado = A * B
    case"/":
        resultado = A / B
    case _:
        print("Opção invalida")
    
#   Exibindo Resultados
print()
print(f"Primeiro número: {A}")
print(f"Operação: {operacao}")
print(f"Segundo número: {B}")
print(f"Resultado: {resultado}")