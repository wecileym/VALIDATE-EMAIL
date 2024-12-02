from tkinter import messagebox
import re
import tkinter as tk
import customtkinter as ctk


class Logon(ctk.CTk): 

    def __init__(self):
        super().__init__()
        
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        self.geometry("800x600")
        self.minsize(800, 600)
        self.title('Login')
        
        self.email = ctk.CTkEntry(self, width=480, height=50, font=('Century Gothic', 20,'bold'))
        self.email.pack(pady=5, padx=10)
        self.email.bind("<FocusOut>", lambda event: self.validate_email(event, self.email))

        self.anything = ctk.CTkEntry(self, width=480, height=50, font=('Century Gothic', 20,'bold'))
        self.anything.pack(pady=5, padx=10)

    def validate_email(self, event, entry):
        email = entry.get()
        if not self.is_valid_email(email):
            messagebox.showerror("Erro de entrada", "Por favor, insira um email válido.")
            entry.delete(0, tk.END)
            return

    def is_valid_email(self, email):
        # Verifica se o email tem pelo menos um caractere antes de @, um @, pelo menos um caractere depois de @,
        # um ponto após @, e pelo menos dois caracteres após o ponto
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None


if __name__ == "__main__":
    logon = Logon()
    logon.mainloop()
    
   