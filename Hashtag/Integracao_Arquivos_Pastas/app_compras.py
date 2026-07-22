import json
import time
import os


def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade

def remover_item(compras, item):
    if item in compras:
        del compras[item]

def visualizar_compras(compras):
    for item, quantidade in compras.items():
        print(f"{item}: {quantidade}")
    print()
    print("Pressione Enter para continuar...")
    input()

def salvar_compras(compras, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(compras, arquivo)

def carregar_compras(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return json.load(arquivo)

def gerenciar_compras(compras, nome_arquivo=None):
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Visualizar lista de compras")
        print("4. Salvar lista de compras e sair")
        print("5. Sair sem salvar")
        
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            item = input("Digite o nome do item: ")
            quantidade = int(input("Digite a quantidade: "))
            adicionar_item(compras, item, quantidade)
        elif escolha == '2':
            item = input("Digite o nome do item a ser removido: ")
            remover_item(compras, item)
        elif escolha == '3':
            visualizar_compras(compras)
        elif escolha == '4':
            if nome_arquivo is None:
                nome_arquivo = input("Digite o nome do arquivo para salvar: ")
            if not nome_arquivo.endswith('.json'):
                nome_arquivo += '.json'
            salvar_compras(compras, nome_arquivo)
            break
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(1)

def main():
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Criar uma nova lista de compras")
        print("2. Carregar uma lista existente")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            compras = {}
            gerenciar_compras(compras)
            
        elif escolha == '2':
            print("Listas disponíveis:")
            arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith('.json')]
            if not arquivos:
                print("Nenhuma lista de compras encontrada.")
                time.sleep(2)
                continue

            for i, arquivo in enumerate(arquivos):
                print(f"{i}. {arquivo}")
            escolha = int(input("Escolha uma lista para carregar (0 se nenhum): "))
            if escolha == '0':
                continue
            if escolha < 0 or escolha > len(arquivos):
                print("Opção inválida. Tente novamente.")
                continue
            time.sleep(2)
            nome_arquivo = arquivos[escolha - 1]
            compras = carregar_compras(nome_arquivo)
            gerenciar_compras(compras, nome_arquivo)
        elif escolha == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(1)

if __name__ == "__main__":
    main()