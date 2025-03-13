import pyperclip
import time
from googletrans import Translator
import tkinter as tk

import pyperclip
import time
from googletrans import Translator
import tkinter as tk
import re

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traductor")
        self.root.geometry("400x200")
        self.root.attributes('-alpha', 0.8)  # Hace la ventana semitransparente
        self.root.attributes('-topmost', True)  # Mantiene la ventana siempre encima
        
        self.traductor = Translator()  # Crear una única instancia del traductor
        self.texto_copiado = ""
        
        self.label_original = tk.Label(root, text="Texto copiado:", font=("Arial", 12))
        self.label_original.pack(pady=5)
        
        self.texto_original = tk.Label(root, text="", wraplength=350, font=("Arial", 10), fg="blue")
        self.texto_original.pack()
        
        self.label_traducido = tk.Label(root, text="Traducción:", font=("Arial", 12))
        self.label_traducido.pack(pady=5)
        
        self.texto_traducido = tk.Label(root, text="", wraplength=350, font=("Arial", 10), fg="green")
        self.texto_traducido.pack()
        
        self.actualizar_traduccion()
    
    def es_url(self, texto):
        
        patron_url = re.compile(
            r'^(https?:\/\/)?'          
            r'(www\.)?'                 
            r'([a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+)' 
            r'(\/\S*)?$'                
        )
        return patron_url.match(texto) is not None

    def traducir(self, texto):
        try:
            traduccion = self.traductor.translate(texto, src="en", dest="es")
            return traduccion.text
        except Exception as e:
            return "Error en la traducción"
    
    def actualizar_traduccion(self):
        nuevo_texto = pyperclip.paste().strip()
        if nuevo_texto and nuevo_texto != self.texto_copiado:
            self.texto_copiado = nuevo_texto
            if self.es_url(nuevo_texto):
                texto_traducido = nuevo_texto
            else:
                texto_traducido = self.traducir(nuevo_texto)
            self.texto_original.config(text=nuevo_texto)
            self.texto_traducido.config(text=texto_traducido)
        self.root.after(1000, self.actualizar_traduccion)  
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
