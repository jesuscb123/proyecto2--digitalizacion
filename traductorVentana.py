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
        self.root.title("Translator")
        self.root.geometry("400x200")
        self.root.attributes('-alpha', 0.8)  # Makes the window semi-transparent
        self.root.attributes('-topmost', True)  # Keeps the window always on top
        
        self.translator = Translator()  # Create a single instance of the translator
        self.copied_text = ""
        
        self.original_label = tk.Label(root, text="Copied Text:", font=("Arial", 12))
        self.original_label.pack(pady=5)
        
        self.original_text = tk.Label(root, text="", wraplength=350, font=("Arial", 10), fg="blue")
        self.original_text.pack()
        
        self.translated_label = tk.Label(root, text="Translation:", font=("Arial", 12))
        self.translated_label.pack(pady=5)
        
        self.translated_text = tk.Label(root, text="", wraplength=350, font=("Arial", 10), fg="green")
        self.translated_text.pack()
        
        self.update_translation()
    
    def is_url(self, text):
        """
        Checks if the given text is a URL.
        
        Parameters:
            text (str): The text to be checked.
        
        Returns:
            bool: True if the text is a URL, False otherwise.
        """
        url_pattern = re.compile(
            r'^(https?:\/\/)?'          
            r'(www\.)?'                 
            r'([a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+)' 
            r'(\/\S*)?$'                
        )
        return url_pattern.match(text) is not None

    def translate(self, text):
        """
        Translates text from English to Spanish.
        
        Parameters:
            text (str): The text to be translated.
        
        Returns:
            str: The translated text, or an error message if translation fails.
        """
        try:
            translation = self.translator.translate(text, src="en", dest="es")
            return translation.text
        except Exception as e:
            return "Translation Error"

    def update_translation(self):
        """
        Periodically checks the clipboard for new text.
        If new text is found, it translates and updates the labels.
        """
        new_text = pyperclip.paste().strip()
        if new_text != self.copied_text:
            self.copied_text = new_text
            if self.is_url(new_text):
                translated_text = new_text
            else:
                translated_text = self.translate(new_text)
            self.original_text.config(text=new_text)
            self.translated_text.config(text=translated_text)
        self.root.after(1000, self.update_translation)  


def main():
    """
    Launches the application window and starts the main loop.
    """
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
        
if __name__ == "__main__":
    main()
