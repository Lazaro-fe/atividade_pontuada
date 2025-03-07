# Limpeza do Terminal
import os
os.system("clear")

# Solicitando dados ao Usuário 

nome = input("Digite seu nome : ")
sexo = input ("Digite o sexo no qual você se identifica : ").lower()
estado_civil = input("Digite o seu estado cívil : ")

# Processando 

print()

if sexo == "f" and estado_civil == "casada" :
    tempo_de_conjuge = input("Há quanto tempo você está casada : ")
elif sexo == "m" and estado_civil == "casado":
    tempo_de_conjuge = input("Há quanto tempo você está casado : ")
if sexo == "f" and estado_civil == "solteiro":
    print("Tenha paciência! (= )")
elif sexo == "m" and estado_civil == "solteiro":
    print("Tenha paciência mano! (= )")
else :
    tempo_de_conjuge = "Não se aplica"

print()
print(f"Nome : {nome}")
print(f"Sexo : {sexo}")
print(f"estado civil : {estado_civil}")
print(f"Tempo de casada : {tempo_de_conjuge}")