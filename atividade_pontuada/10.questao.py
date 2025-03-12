# Limpeza do Terminal
import os
os.system("clear")

# Solicitando dados ao Usuário

tipo_de_combustivel = input("Digite o tipo de combustível : ")
quantidade_de_combustivel_vendido = int(input("Digite a quantidade de combustível vendido : "))

valor_a_ser_pago = quantidade_de_combustivel_vendido

# Verificando

match tipo_de_combustivel :
    case "A-alcool" :
        if quantidade_de_combustivel_vendido > 25 :
            total = quantidade_de_combustivel_vendido * 3.79 * 0.04
        elif quantidade_de_combustivel_vendido <= 25 :
            total = quantidade_de_combustivel_vendido * 3.79 * 0.02
    case "G-gasolina" :
        if quantidade_de_combustivel_vendido > 25 :
            total = quantidade_de_combustivel_vendido * 6.59 * 0.05
        elif quantidade_de_combustivel_vendido <= 25 :
            total = quantidade_de_combustivel_vendido * 6.59 * 0.03

# Exibindo Resultados 

print()
print(f"Tipo de combustivel escolido {tipo_de_combustivel}")
print(f"Quantidade de conbustível {quantidade_de_combustivel_vendido}")
print(f"Total á pagar : {total}")