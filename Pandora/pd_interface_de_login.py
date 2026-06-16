import customtkinter as ctk
from pd_criar_conta import criar_conta
from customtkinter import *
import sqlite3
from pd_interface import pd_interface
from PIL import Image


def pd_login():
    #função1
    def janela_de_login():
        janela_1.destroy()

        #criação da janelafazer login
        ctk.set_appearance_mode("dark")
        janela_2 = ctk.CTk()
        janela_2.title("Faça login no Pandora")
        janela_2.geometry("1366x768")
        janela_2.config(background="#000000")
        janela_2.resizable(
            width= False,
            height= False
        )

        #inicio da janela fazer login
        # 
        # 
        #  
        #label de texto login

        
        imagem = ctk.CTkImage(
            Image.open("imagens/pandora_1.png"),
            size= (120,120)
            )
        
        logo = ctk.CTkLabel(
            janela_2,
            bg_color="#000000",
            text=None,
            width= 150,
            height=150,
            image=imagem
        )
        logo.place(
            x=600,
            y=20
        )


        texto_login = ctk.CTkLabel(
            janela_2,
            text= "Faça login no Pandora",
            bg_color="#000000",
            font = ctk.CTkFont(
                "DjaVu Sans",
                20,
                "bold"
            )
        )
        texto_login.place(
            y=175,
            x=550
        )

        #label de nome e email
        texto_login_1 = ctk.CTkLabel(
            janela_2,
            text= "Nome de usuário ou endereço de e-mail",
            bg_color="#000000",
            font = ctk.CTkFont(
                "DjaVu Sans",
                12,
                "bold"
            )
        )
        texto_login_1.place(
            x=483,
            y=234
        )
        #entry de nome e e-mail
        caixa_de_nome = CTkEntry(
            janela_2,
            corner_radius=10,
            width= 410,
            height= 45,
            border_width= 1,
            border_color="#2A2A2A",
            bg_color="#000000",
            fg_color="#000000"
        )
        caixa_de_nome.place(
            x=480,
            y=255
        )
        #label DE TEXTO DE SENHA
        texto_login_2 = ctk.CTkLabel(
            janela_2,
            text= "Senha",
            bg_color="#000000",
            font = ctk.CTkFont(
                "DjaVu Sans",
                12,
                "bold"
            )
        )
        texto_login_2.place(
            x=483,
            y=316
        )
        #entry
        caixa_de_nome_1 = CTkEntry(
            janela_2,
            show= "*",
            corner_radius=10,
            width= 410,
            height= 45,
            border_width= 1,
            border_color="#2A2A2A",
            bg_color="#000000",
            fg_color="#000000"
        )
        caixa_de_nome_1.place(
            x=480,
            y=337
        )

        #botão criar uma conta
        botao_conta = ctk.CTkButton(
            janela_2,
            bg_color = "#000000",
            fg_color = "#000000",
            text_color = "#4242E7",
            text = "Crie uma conta.",
            hover = None,
            font= ctk.CTkFont(
                "DejaVu Sans",
                12,
            ),
            command=lambda:criar_conta(janela_2)
        )
        botao_conta.place(
            x=675,
            y=470
        )

        #label é novo no pandora?
        texto_login_3 = ctk.CTkLabel(
            janela_2,
            bg_color = "#000000",
            text="É novo no Pandora?",
            font= ctk.CTkFont(
                "DejaVu Sans",
                12,
            )
        )
        texto_login_3.place(
            x=570,
            y=470
        )

        def fazer_login():
            usuario = caixa_de_nome.get()
            senha = caixa_de_nome_1.get()

            conexao= sqlite3.connect("pd_login.db")
            cursor= conexao.cursor()


            cursor.execute("""
                    SELECT * FROM usuarios
                    WHERE (NOME = ? OR EMAIL = ?)
                    AND SENHA = ?
                """, (usuario, usuario, senha))
            
            resultado = cursor.fetchone()

            conexao.close()

            if resultado:
                pd_interface(janela_2)

            else:
                erro = ctk.CTkLabel(
                janela_2,
                text="Usuário ou senha incorretos!",
                bg_color="#000000",
                text_color="red"
            )
            erro.place(x=600, y=510)

        #botao de entrar
        botao_entrar = ctk.CTkButton(
            janela_2,
            corner_radius=10,
            text = "Entrar",
            command= fazer_login,
            font = ctk.CTkFont(
                "DjaVu Sans",
                12,
                "bold"
            ),
            width= 410,
            height= 45,
            bg_color="#000000",
            fg_color ="#3F812F",
            hover_color = "#356D28",
        )
        botao_entrar.place(
            x=480,
            y=415
        )
        janela_2.mainloop()

        #função2
    #fim da função de trocar janela e criaçao da janela de login


    #janela 1 criação da janela continuar
    ctk.set_appearance_mode("dark")
    janela_1 = ctk.CTk()
    janela_1.title("Bem vindo ao Pandora")
    janela_1.geometry("1366x768")
    janela_1.config(background="#020202")
    janela_1.resizable(
        width= True,
        height= True
    )

    texto_1 = ctk.CTkLabel(
        janela_1,
        text= "Bem vindo ao Pandora",
        bg_color="#020202",
        font = ctk.CTkFont(
            "DjaVu Sans",
            40,
            "bold"
        )
    )
    texto_1.pack(
        pady=80
    )

    #botao de entrar
    botao_continuar = ctk.CTkButton(
        janela_1,
        corner_radius=12,
        text_color= "#000000",
        text = "Continuar",
        font = ctk.CTkFont(
            "DjaVu Sans",
            17,
            "bold"
        ),
        width= 460,
        height= 60,
        bg_color="#020202",
        fg_color ="#FFFFFF",
        hover_color = "#B3B3B3",
        command=janela_de_login
    )
    botao_continuar.pack(
        pady=0
    )


    janela_1.mainloop()

