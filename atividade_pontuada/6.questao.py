#Limpa o Terminal
import os
os.system("clear")

# Solicitando os dados para o usuário
nome = input("Qual o seu nome ? ")
n1 = float(input("Digite a nota de seu teste : "))
n2  = float(input("Digite a nota da sua prova : "))

media = (n1 + n2) / 2

# Processando

match media:
    case 1:
        if media >= 6.0:
            resultado = "Você está Aprovado!! Parabéns ( = "
    case 2:
        if media < 4.0:
            resultado = "Você foi reprovado!!!"
    case _:
        resultado = "Você foi aprovado"

# Exibindo Resultados 

print()
print(f"Média : {media}")
print(f"Resultado : {resultado}")