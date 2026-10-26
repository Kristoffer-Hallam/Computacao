# Exercício retirado do Curso de Especialização em Python da Hashtag para

import os
import sys
import time

import pandas as pd

os.system("cls" if os.name == "nt" else "clear")

# Exercícios

## 1. Cálculo do Percentual e da Lista de Vendedores

# - Queremos criar uma function que consiga identificar os vendedores que bateram uma meta,
# mas além disso, consigo já me dar como resposta o cálculo do % da lista de vendedores que
# bateu a meta (para eu não precisar calcular manualmente depois)
# - Essa function deve receber 2 informações como parâmetro: a meta e um dicionário com os
# vendedores e suas vendas. E me dar 2 respostas: uma lista com o nome dos vendedores que
# bateram a meta e o % de vendedores que bateu a meta.

meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}

def bateram_meta(meta, vendas):
    vendedores_bateram_meta = [vendedor for vendedor, venda in vendas.items() if venda >= meta]
    percentual_bateram_meta = len(vendedores_bateram_meta) / len(vendas) * 100
    return vendedores_bateram_meta, percentual_bateram_meta

vendedores_bateram_meta, percentual_bateram_meta = bateram_meta(meta, vendas)
print()
print(f"Vendedores que bateram a meta: {vendedores_bateram_meta}")
print(f"Percentual de vendedores que bateram a meta: {percentual_bateram_meta:.2f}%")
print()