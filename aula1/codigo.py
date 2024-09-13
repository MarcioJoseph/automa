# escreva o passo a passo do projeto para ter uma direção a seguir 

# passo 1 - entrar no sistema da empresa
    # link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# passo 2 - fazer o login
# passo 3 - pegar/importar a base de dados 
# passo 4 - cadastrar um produto
# passo 5 - repetir o passo 4 até cadastrar todos os produtos

import pyautogui
# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto 
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de teclas (ctrl c)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5
import time

# passo 1 - entrar no sistema
# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link - https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# passo 2 - fazer o login
pyautogui.click(x=372, y=444)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("zetasnk@hotmail.com")

# passar para o campo de senha
pyautogui.press("tab")
pyautogui.write("coxinha123")
pyautogui.click(x=492, y=588)
time.sleep(3)

# passo 3 - importar a base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# passo 4 - cadastrar um produto
# para cada linha da minha tabela:
for linha in tabela.index:
    # codigo
    pyautogui.click(x=299, y=338)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    
    # marca
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    
    # tipo
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    # categoria
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    
    # preco_unitario
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    
    # custo
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    
    # obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    
    # clicar no botão enviar
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# passo 5 - repetir o passo 4 até cadastrar todos os produtos
# codigo da aula 1 - aprendapython
