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
    """
    Simple translator app that checks the clipboard every second.
    If it finds new text, it translates it from English to Spanish
    and shows both the original and translated text in a small window.
    """    
    def __init__(self, root):
        """
        Sets up the app window and UI elements.
        
        Parameters:
            root (tk.Tk): The main window of the application.
        """
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
        """
        Checks if the given text is a URL.
        
        Parameters:
            text (str): The text to be checked.
        
        Returns:
            bool: True if the text is a URL, False otherwise.
        """
        patron_url = re.compile(
            r'^(https?:\/\/)?'          
            r'(www\.)?'                 
            r'([a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+)' 
            r'(\/\S*)?$'                
        )
        return patron_url.match(texto) is not None

    def traducir(self, texto):
        """
         Translates text from English to Spanish.
        
        Parameters:
            text (str): The text to be translated.
        
        Returns:
            str: The translated text, or an error message if translation fails.
        """
        try:
            traduccion = self.traductor.translate(texto, src="en", dest="es")
            return traduccion.text
        except Exception as e:
            return "Error en la traducción"

    def actualizar_traduccion(self):
        """
        Periodically checks the clipboard for new text.
        If new text is found, it translates and updates the labels.
        """
        nuevo_texto = pyperclip.paste().strip()
        if nuevo_texto != self.texto_copiado:
            self.texto_copiado = nuevo_texto
            if self.es_url(nuevo_texto):
                texto_traducido = nuevo_texto
            else:
                texto_traducido = self.traducir(nuevo_texto)
            self.texto_original.config(text=nuevo_texto)
            self.texto_traducido.config(text=texto_traducido)
        self.root.after(1000, self.actualizar_traduccion)  


def main():
        """
        Launches the application window and starts the main loop.

        """
        root = tk.Tk()
        app = TranslatorApp(root)
        root.mainloop()
        
if __name__ == "__main__":
    main()
