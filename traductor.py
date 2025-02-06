import pyperclip
import time
from googletrans import Translator
import tkinter as tk
import os

def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def pausa():
    time.sleep(0.2)

def copiar_texto():
    texto_copiado = pyperclip.paste()
    return texto_copiado

def traducir(texto_copiado: str):
    traductor = Translator()
    traduccion = traductor.translate(texto_copiado, src = "en", dest="es")
    return traduccion



def actualizar_textoanterior(texto_diferente: bool,texto_copiado: str,texto_anterior: str)->str:
    while not texto_diferente:
        texto_diferente = comprobar_texto(texto_copiado,texto_anterior)
        if texto_diferente == False:
            texto_copiado = copiar_texto()
            pausa()
    texto_anterior = texto_copiado
    return texto_anterior,texto_copiado


def comprobar_texto(texto_copiado: str, texto_anterior: str):
    if texto_anterior != texto_copiado:
        return True
    else:
        return False
    


def main():
    texto_anterior = ""
    salir = False
    while not salir:
        texto_diferente = False
        texto_copiado = copiar_texto()
        texto_anterior,texto_copiado = actualizar_textoanterior(texto_diferente, texto_copiado, texto_anterior)
        texto_traducido = traducir(texto_copiado)
        limpiar_pantalla()
        print(f"Portapapeles: {texto_copiado}")
        print(f"Traducción: {texto_traducido.text}")



    
if __name__ == "__main__":
    main()