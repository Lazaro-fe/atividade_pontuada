# Limpeza do Terminal
import os
os.system("clear")

# Solicitando dados ao Usuário

tipo_de_combustivel = input("Digite o tipo de combustível : ")

A_alcool = float(3.79)
G_gasolina = float(6.59)
A_alcool2 = float(3.79)
G_gasolina2 = float(6.59)


# Processando

if quantidade_de_alcool or quantidade_de_gasolina <= 25:
    quantidade_de_gasolina = float(input("Quantidade de gasolina vendida :"))
    total = (quantidade_de_alcool * A_alcool * 0.02) or (quantidade_de_gasolina * G_gasolina * 0.03)
if quantidade_de_alcool or quantidade_de_gasolina >= 25 :
    total = (quantidade_de_alcool * A_alcool * 0.04) or (quantidade_de_gasolina * G_gasolina2 * 0.05)

# Exbindo Resultados 

print()
print(f"Tipo de Combustivel vendido : {tipo_de_combustivel}")
print(f"Quantidade de Combustível vendido : {A_alcool or G_gasolina}")
print(f"Total de Combustível vendido : {total}")