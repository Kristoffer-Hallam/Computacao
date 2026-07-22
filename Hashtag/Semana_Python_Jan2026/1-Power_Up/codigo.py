import os
import sys
import time
import json
import pandas as pd
import numpy as np
import pyautogui
import pyperclip
from pynput.mouse import Controller, Button

def open_safari():
    pyautogui.click(x=165, y=735)  # Clica no Dock sobre o ícone do Launchpad
    pyautogui.click(x=339, y=108)  # Clica no ícone do Safari
    # pyautogui.click(x=1307, y=56)  # Clica no ícone de nova aba
    time.sleep(3)
    pyautogui.hotkey('command', 't') # Cria nova aba
    
def pega_coords():
    time.sleep(3)
    print(pyautogui.position())
    
if __name__ == "__main__":
    os.system('clear')
    os.system('reset')
    
    pyautogui.PAUSE = 1  # Pausa de 1 segundo entre as ações do PyAutoGUI
    open_safari()
    
    # Link da pagina para ser preenchida
    link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    pyperclip.copy(link)
    pyautogui.hotkey('command', 'v')  # Cola o link na barra de endereços
    pyautogui.press('enter')  # Pressiona Enter
    time.sleep(5)  # Espera a página carregar
    
    # Clicar no campo de login
    pyautogui.click(x=568, y=396)
    pyautogui.write("pythonimpressionador@gmail.com")
    pyautogui.press("tab") # passando pro próximo campo
    pyautogui.write("sua senha")
    # pyautogui.click(x=692, y=552) # clique no botao de login
    pyautogui.press("enter")  # Pressiona Enter
    time.sleep(3)  # Espera a página carregar
    pyautogui.click(x=699, y=494) # clique no botao de "Agora Não"
    
    # Lendo arquivo csv
    df = pd.read_csv("produtos.csv")
    
    # print(df.head())
    rows = [tuple(row) for row in df.itertuples(index=False, name=None)]
    
    # Pegando coordenadas dos campos dos formularios
    for j, row in enumerate(rows):
        pyautogui.click(x=644, y=279) # clicando no campo código do produto        
        # print(row)
        row = list(row)  # Convert tuple to list so we can modify it
        for i in range(len(row)):
            if not isinstance(row[i], str):
                if np.isnan(row[i]):
                    row[i] = ""
            if j == 0:
                pyperclip.copy(str(row[i])) # O primeiro item está sendo pulado sempre
            else:
                pyperclip.copy(str(row[i]))
            pyautogui.hotkey('command', 'v')  # colando o item no campo
            # time.sleep(0.5)
            pyautogui.press("tab")  # passando pro próximo campo
            
        # Clicando no botao de enviar
        # pyautogui.click(x=613, y=562)
        pyautogui.press("tab")  # passando pro próximo campo
        pyautogui.press("enter")  # Pressiona Enter
        time.sleep(1)
        # Clicando no botao de limpar
        # pyautogui.click(x=790, y=579)
        # time.sleep(1)
        # Scrolling upvoltando a pagina para o topo
        pyautogui.scroll(500)
        time.sleep(1)
        # break
    
    # time.sleep(5)
    # pega_coords()
    # sys.exit()