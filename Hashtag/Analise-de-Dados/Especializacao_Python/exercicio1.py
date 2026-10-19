# Exercício retirado do Curso de Especialização em Python da Hashtag para
# Análise de Dados - aula "Criando suas funções"
#
# Exercícios de Function - Exercicios 1

import os

os.system("cls" if os.name == "nt" else "clear")

# Imagine que você trabalhe no setor contábil de uma empresa de Varejo.
# Crie uma função que calcule qual a porcentagem de carga tributária que está sendo aplicado
# a um determinado produto, dado o preço de venda e os custos. OBS: Repare que o preço menos
# o custo não será igual ao lucro, pois deve-se descontar o imposto cobrado. Sua função deve
# calcular qual foi a porcentagem de imposto aplicado sobre o preço total.

def calcular_carga_tributaria(preco=1500, custo=400, lucro_real=800):
    
    print(f"O lucro do produto é de {preco - custo:.2f}. ")
    print(f"O lucro real do produto é de {lucro_real:.2f}. ")
    
    imposto = preco - custo - lucro_real
    print(f"O imposto calculado é de {imposto:.2f}. ")
    
    if lucro_real is None:
        carga_tributaria = 0
    else:
        carga_tributaria = imposto / preco
        
    return carga_tributaria

default = input("Usar os valores padrão (preço=1500, custo=400, lucro_real=800)? (s/n): ")
if default == "s":
    carga_tributaria = calcular_carga_tributaria()
else:
    preco = float(input("Dê o valor do preço de venda do produto: "))
    custo = float(input("Dê o valor do custo do produto: "))
    lucro_real = float(input("Dê o valor do lucro real do produto: "))
    carga_tributaria = calcular_carga_tributaria(preco, custo, lucro_real)
    
print(f"A carga tributária aplicada sobre o preço total é de {carga_tributaria*100:.2f}%.")