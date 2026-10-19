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