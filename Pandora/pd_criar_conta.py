import sqlite3
import customtkinter as ctk
from customtkinter import * 
from sqlite3 import *
from retornar_login import janela_de_login_1


def criar_conta(janela):
    janela.destroy()

    conexao = sqlite3.connect("pd_login.db")
    cursor = conexao.cursor()

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    janela_2 = ctk.CTk()
    janela_2.title("Cadastre-se no Pandora")
    janela_2.geometry("520x560")
    janela_2.config(background="#0F0F0F")
    janela_2.resizable(
            width=False,
            height=False
    )
                    
    frame_1 = ctk.CTkFrame(
     janela_2,
    corner_radius= 20,
    fg_color="#111111",
     bg_color="#0F0F0F",
    width=500,
    height=540
    )
    frame_1.pack(
            pady=10
    )

    texto_conta = ctk.CTkLabel(
            frame_1,
            text= "Cadastre-se no Pandora!",
            bg_color="#111111",
            font= ctk.CTkFont(
                    "DejaVu Sans",
                    20,
                    "bold"
        )
    )
    texto_conta.place(
            x= 110,
            y= 0
    )


    texto_usuario = ctk.CTkLabel(
            frame_1,
            text= "Digite seu usuario",
            font= ctk.CTkFont(
                    "DejaVu Sans",
                    10,
                    "bold"
        )
    )
    texto_usuario.place(
            x=47,
            y=40
                )

    texto_email = ctk.CTkLabel(
            frame_1,
            text= "Digite seu endereço de e-mail",
            font= ctk.CTkFont(
            "DejaVu Sans",
            10,
            "bold"
        )
    )
    texto_email.place(
            x=47,
            y=120
    )


    texto_senha = ctk.CTkLabel(
            frame_1,
            text= "Digite sua senha",
            font= ctk.CTkFont(
                    "DejaVu Sans",
                    10,
                    "bold"
        )
    )
    texto_senha.place(
            x=47,
            y=200
    )


    caixa_de_usuario = ctk.CTkEntry(
            frame_1,
            corner_radius=10,
            width= 410,
            height= 45,
            bg_color="#111111",
            fg_color="#111111"
    )
    caixa_de_usuario.place(
            x=45,
            y=60
    )


    caixa_de_email = ctk.CTkEntry(
            frame_1,
            corner_radius=10,
            width= 410,
            height= 45,
            bg_color="#111111",
            fg_color="#111111"
    )
    caixa_de_email.place(
            x=45,
            y=140
        )

    caixa_de_senha = ctk.CTkEntry(
            frame_1,
            corner_radius=10,
            width= 410,
            height= 45,
            bg_color="#111111",
            fg_color="#111111"
    )
    caixa_de_senha.place(
            x=45,
            y=220
        )
    
    def salvar():
        nome= caixa_de_usuario.get()
        email= caixa_de_email.get()
        senha= caixa_de_senha.get()

        if nome == "" or email == "" or senha == "":
            erro_1 = ctk.CTkLabel(
                frame_1,
                text= "Prenche todos os campos!",
                text_color="#FF0000",
                )

            erro_1.place(
                x= 170,
                y=350
            )

            return
        
        
        cursor.execute("INSERT INTO usuarios (NOME, EMAIL, SENHA) VALUES (?, ?, ?)",
            (nome, email, senha))
        
        conexao.commit()

        janela_2.destroy()

        ctk.set_appearance_mode("dark")
        janela_sucesso = ctk.CTk()
        janela_sucesso.title("Sucesso")
        janela_sucesso.geometry("400x300")
        janela_sucesso.config(background="#0F0F0F")
        janela_sucesso.resizable(
                    width= False,
                    height= False
                )

        texto = ctk.CTkLabel(
                janela_sucesso,
                bg_color="#0F0F0F",
                text="Conta criada com sucesso!",
                font=ctk.CTkFont(
                    "DejaVu Sans",
                    16,
                    "bold")
        )
        texto.pack(pady=40)

        botao_fazer_login = ctk.CTkButton(
            janela_sucesso,
            text= "Fazer login",
            command= lambda:janela_de_login_1(janela_sucesso),
            width= 210,
            height= 45,
            fg_color ="#3F812F",
            hover_color="#356D28"
        )

        botao_fazer_login.pack(
            pady=0
        )

        janela_sucesso.mainloop()
                
    botao_criar = ctk.CTkButton(
            frame_1,
            width= 210,
            height= 45,
            text = "Cadastrar",
            command= salvar,
            bg_color="#111111",
            fg_color ="#3F812F",
            hover_color="#356D28"
    )
    botao_criar.place(
            x= 45,
            y= 290
    )

    janela_2.mainloop
