# Limpeza do Terminal
import os
os.system("clear")

# Solicitando dados ao Usuário 

nome_do_produto = input("Digite o nome do produto : ")
quantidade = int(input("Digite a quantidade do produto adquirido : "))
preco_do_produto = float(input("Digite o valor do produto : "))

total = quantidade * preco_do_produto
desconto = total * 0.02 or total * 0.03 * total * 0.05

match quantidade :
    case 1: 
        if quantidade <= 5 :
            desconto = total * 0.02
    case 2:
        if quantidade > 5 and quantidade <= 10:
            desconto = total * 0.03
    case 3:
        if quantidade > 10 :
            desconto = total * 0.05

pagamento_total = total - desconto

# Exibindo Resultados

print()
print(f"Nome do produto : {nome_do_produto}")
print(f"Quantidade do Produto : {quantidade:.2f}")
print(f"Preço do Produto : {preco_do_produto:.2f}")
print(f"Total : {total}")
print(f"Desconto : {desconto:.2f}")
print(f"Total à pagar : {pagamento_total:.2f}")