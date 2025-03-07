# Limpeza do Terminal
import os
os.system("clear")

# Solicitando dados ao Usuário

print("""

=============================== TABELA DE PREÇOS ===============================

                \tAté 5 kg                       \tAcima de 5 kg

\tMORANGO      \tR$ 2,50 POR KG                   \tR$ 2,20 POR KG  

\tMAÇÃ         \tR$ 1,80 POR KG                    \tR$ 1,50 POR KG
""")

quantidade_de_morango = float(input("Diga a quantidade de morango : "))
quantidade_de_maca = float(input("Diga a quantidade de maçãs : "))

maca = float(2.50)
maca_2 = float(2.20)
morango = float(1.80)
morango_2 = float(1.50)

# Exibindo resultados 

if quantidade_de_maca or quantidade_de_morango < 5:
    total = (quantidade_de_morango * morango) + (quantidade_de_maca * maca)
    print(f"Total : {total}")
elif quantidade_de_maca or quantidade_de_morango > 5:
    total_comprado = (quantidade_de_morango * morango_2) + (quantidade_de_maca * maca_2)
    print(f"Total da Comprado : {total_comprado}")