import os
import sys
from pathlib import Path
import shutil

import pandas as pd

# Definir o diretório de trabalho
##  os.getcwd() == Path.cwd()

diretorio_trabalho = os.path.join(os.getcwd(), 'Arquivos_Lojas')
work_dir = Path('Arquivos_Lojas')
print(f'Diretório de trabalho: {diretorio_trabalho}')
print(f'Diretório de trabalho: {work_dir}')
print('\n\n')
# Listar arquivos na pasta Arquivos_Lojas
##  os.listdir(diretorio_trabalho) == list(Path(diretorio_trabalho).iterdir())
if os.path.exists(diretorio_trabalho):
    # arquivos = os.listdir(diretorio_trabalho)
    arquivos = work_dir.iterdir()
    print(f'\nArquivos encontrados na pasta Arquivos_Lojas:')
    for arquivo in arquivos:
        print(f'  - {arquivo}')
    # print(f'\nTotal de arquivos: {len(arquivos)}')
else:
    print(f'Diretório {diretorio_trabalho} não existe!')
    
    
if (work_dir / Path("202002_BH Shopping_MG.csv")).exists():
    # Carregar arquivo CSV específico
    arquivo_csv = Path("Arquivos_Lojas/202002_BH Shopping_MG.csv")
    df_bh_shopping = pd.read_csv(arquivo_csv)
    print(f'\nDados do arquivo {arquivo_csv.name}:')
    print(df_bh_shopping.head())
    
# Criando pasta auxiliar
Path('Pasta_Auxiliar').mkdir(exist_ok=True)

# Copiando arquivo para a pasta auxiliar usando shutil
arquivo_copiar = Path("Arquivos_Lojas/202002_BH Shopping_MG.csv")
destino = Path('Pasta_Auxiliar') / "202002_BH Shopping_MG_versao2.csv"
shutil.copy2(arquivo_copiar, destino)
print(f'\nArquivo {arquivo_copiar.name} copiado para Pasta_Auxiliar.')

# Movendo arquivo para a pasta auxiliar usando shutil
shutil.move(
    Path('Pasta_Auxiliar') / "202002_BH Shopping_MG_versao2.csv", Path('Pasta2') / "202002_BH Shopping_MG_versao2.csv"
)
print(f'Arquivo {arquivo_copiar.name} movido para Pasta2.')