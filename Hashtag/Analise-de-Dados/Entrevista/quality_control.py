import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

from rich import print

os.system("clear")
os.system("reset")

# Lendo a primeira aba "POZO"
df = pd.read_excel("Wells_exercise.xlsx")
print(df.head())
print()
print(df.info())

for col in df.columns:
    print(f'Coluna: {col} - Tipo: {df[col].dtype}')
    print(f'Valores faltantes: {df[col].isnull().sum()}')
    print()

print("\n\n")
print(df[['POZO', 'CAMPO', 'UBICACIóN', 'CLASIFICACIóN', 'ESTADO ACTUAL']])
print("\n\n")
print(df[['TIPO DE HIDROCARBURO', 'FECHA INICIO PERFORACIóN', 'FECHA FIN PERFORACIóN']])
print("\n\n")
print(df[['PROFUNDIDAD TOTAL (m)', 'PROFUNDIDAD VERTICAL (m)', 'TRAYECTORIA']])
print("\n\n")


## ANALISE DOS DADOS da primeira tabela

# verificando a coluna CAMPO
print('[green]Valores faltantes da coluna CAMPO:[/green]')
print(df[df['CAMPO'].isna()])
print()

# Criando dicionario com valores únicos das colunas do tipo object
dic = {}
for col in df.columns:
    dic = {col: df[col].unique() for col in df.columns if df[col].dtype == 'object'}

print(dic)
print('\n')
print(dic['FECHA INICIO PERFORACIóN'])
tipo_init = set(type(x) for x in dic['FECHA INICIO PERFORACIóN'])
print(tipo_init)
print()
print(dic['FECHA FIN PERFORACIóN'])
tipo_fim = set(type(x) for x in dic['FECHA FIN PERFORACIóN'])
print(tipo_fim)


# Transformando coluna vertical em float para futuras análises
for vert_value in dic['PROFUNDIDAD VERTICAL (m)']:
    if type(vert_value) != float and type(vert_value) != int:
        print(vert_value, type(vert_value))
        # Encontrando o índice do valor problemático
        index_problem = df[df['PROFUNDIDAD VERTICAL (m)'] == vert_value].index
        print(index_problem)
print(df.loc[index_problem])
df = df.drop(index_problem)

# Obtendo quantidade de poços direcionais e verticais
df_vert = df[df['TRAYECTORIA'] == 'VERTICAL']
df_dir = df[df['TRAYECTORIA'] == 'DIRECCIONAL']
print('[green]Quantidade de poços verticais:[/green]', len(df_vert))
print('[green]Quantidade de poços direcionais:[/green]', len(df_dir))
print('Soma do total:', len(df_vert) + len(df_dir))
print('FALTANTES:', len(df) - (len(df_vert) + len(df_dir)))
print("\n\n")


# Lendo a segunda aba "COORDINATES"
df2 = pd.read_excel("Wells_exercise.xlsx", sheet_name="Coordinates")
df2.rename(columns={"_Pozo_": "POZO"}, inplace=True)
print(df2.head())
print()
print(df2.info())

# Criando dicionario com valores únicos das colunas do tipo object
dic = {}
for col in df2.columns:
    dic = {col: df2[col].unique() for col in df2.columns if df2[col].dtype == 'object'}

print(dic)
print('\n')

# Transformando a coluna Y em float
for val in df2['Y']:
    if type(val) != float and type(val) != int:
        print(val, type(val))
        # Encontrando o índice do valor problemático
        index_problem = df2[df2['Y'] == val].index
        print(index_problem)
print(df2.loc[index_problem])
df2 = df2.drop(index_problem)
print('\n\n')

# Juntando tabelas
full_df = pd.merge(df, df2, on='POZO', how='left')
print(full_df.head())

subset = full_df[[
    'POZO', 'X', 'Y', 'Elevation', 'TRAYECTORIA', 'TIPO DE HIDROCARBURO',
    'PROFUNDIDAD TOTAL (m)', 'PROFUNDIDAD VERTICAL (m)', 'ESTADO ACTUAL'
    ]]

# Plotando boxplot das coordenadas X e Y
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.boxplot(subset['X'].dropna())
plt.title('Boxplot of X Coordinate')
plt.subplot(1, 2, 2)
plt.boxplot(subset['Y'].dropna())
plt.title('Boxplot of Y Coordinate')
plt.tight_layout()
plt.show()

# Plotando a distribuição geográfica dos poços
plt.scatter(subset['X'], subset['Y'], c='blue', alpha=0.5)
plt.title('Geographical Distribuition of Wells')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis('equal')
plt.show()

# Identificando valores problemáticos nas coordenadas X e Y
# print(subset[subset['X'] > 0])
index_problem = subset[subset['X'] > 0].index
# print(index_problem)
subset = subset.drop(index_problem)
# print(subset[subset['Y'] < 0])
# print(subset[subset['Y'] > 100])
index_problem = subset[subset['Y'] > 100].index
subset = subset.drop(index_problem)

# Refazendo a analise espacial

# Plotando boxplot das coordenadas X e Y
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.boxplot(subset['X'].dropna())
plt.title('Boxplot of X Coordinate')
plt.subplot(1, 2, 2)
plt.boxplot(subset['Y'].dropna())
plt.title('Boxplot of Y Coordinate')
plt.tight_layout()
plt.show()

# Plotando a distribuição geográfica dos poços
plt.scatter(subset['X'], subset['Y'], c='blue', alpha=0.5)
plt.title('Geographical Distribuition of Wells')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis('equal')
plt.show()

# Vert X Hoz wells
vert_x_hoz = subset[subset['TRAYECTORIA'] == 'VERTICAL']
horz_x_hoz = subset[subset['TRAYECTORIA'] == 'DIRECCIONAL']
plt.bar(['Vertical Wells', 'Horizontal Wells'], [len(vert_x_hoz), len(horz_x_hoz)], color=['blue', 'orange'])
# plt.title('Quantidade de Poços Verticais vs Horizontais')
plt.ylabel('Number of Wells')
plt.show()