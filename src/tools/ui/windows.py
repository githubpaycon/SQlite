from tkinter import messagebox
from winsound import MB_ICONHAND, MessageBeep

class Windows:
    @staticmethod
    def janela_finalizado(title: str, message: str):
        messagebox.showinfo(title, message)

    @staticmethod
    def janela_erro(title: str, message: str):
        messagebox.showerror(title, message)

    @staticmethod
    def janela_alerta(title: str, message: str):
        messagebox.showwarning(title, message)
        
    @staticmethod
    def faz_pergunta(title: str, message: str):
        MessageBeep(type=MB_ICONHAND)
        return messagebox.askquestion(title, message)