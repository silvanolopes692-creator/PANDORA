 #1-importando bibliotecas
import customtkinter as ctk
from customtkinter import *

def pd_interface(janela_sucesso_login):
    janela_sucesso_login.destroy()
    #2-tema escuro
    ctk.set_appearance_mode("dark")

    #3-defenir cor padrão
    ctk.set_default_color_theme("dark-blue")

    #4-criação e resolução da janela e titutlo
    janela = ctk.CTk()
    janela.geometry("1366x768")
    janela.config(background="#0F0F0F")
    janela.resizable(
        width= True,
        height= True
    )
    janela.title("Pandora")

    #5-criação do texto de titulo
    titulo = ctk.CTkLabel(
        janela,
        text="Bem vindo ao Pandora!",
        bg_color="#0F0F0F",
        font=ctk.CTkFont("DejaVu Sans", 30, "bold",)
    )
    titulo.pack(
        pady=30
    )

    #criação da caixa de entrada de texto
    

    #caixa lateral esquerda(1)
    

    #caixa de configurações (2)
    

    #mini texto de configurações
    
    
    #mini texto de opções
    

    #caixa de mensagem
    

    #opções de idioma
    
    
    #interroptor (1)
    

    #6-ciração do botão enviar
    

    #7-posição do botão enviar
    
    janela.mainloop()
