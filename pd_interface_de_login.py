import customtkinter as ctk
from pd_criar_conta import criar_conta
from customtkinter import *
import sqlite3
from pd_interface import pd_interface

def pd_login():
    #função1
    def janela_de_login():
        janela_1.destroy()

        #criação da janelafazer login
        ctk.set_appearance_mode("dark")
        janela = ctk.CTk()
        janela.title("Faça login no Pandora")
        janela.geometry("520x560")
        janela.config(background="#0F0F0F")
        janela.resizable(
            width= False,
            height= False
        )

        #inicio da janela fazer login
        # 
        # 
        #  
        #label de texto login
        texto_login = ctk.CTkLabel(
            janela,
            text= "Faça login no Pandora",
            bg_color="#0F0F0F",
            font = ctk.CTkFont(
                "DjaVu Sans",
                20,
                "bold"
            )
        )
        texto_login.pack(
            pady=60
        )

        #label de nome e email
        texto_login_1 = ctk.CTkLabel(
            janela,
            text= "Nome de usuário ou endereço de e-mail",
            bg_color="#0F0F0F",
            font = ctk.CTkFont(
                "DjaVu Sans",
                12,
                "bold"
            )
        )
        texto_login_1.place(
            x=60,
            y=127
        )
        #entry de nome e e-mail
        caixa_de_nome = CTkEntry(
            janela,
            corner_radius=10,
            width= 410,
            height= 45,
            bg_color="#0F0F0F",
            fg_color="#0F0F0F"
        )
        caixa_de_nome.pack(
            pady= 0
        )
        #label DE TEXTO DE SENHA
        texto_login_2 = ctk.CTkLabel(
            janela,
            text= "Senha",
            bg_color="#0F0F0F",
            font = ctk.CTkFont(
                "DjaVu Sans",
                12,
                "bold"
            )
        )
        texto_login_2.place(
            x=60,
            y=211
        )
        #entry
        caixa_de_nome_1 = CTkEntry(
            janela,
            show= "*",
            corner_radius=10,
            width= 410,
            height= 45,
            bg_color="#0F0F0F",
            fg_color="#0F0F0F"
        )
        caixa_de_nome_1.pack(
            pady= 40
        )

        #botão criar uma conta
        botao_conta = ctk.CTkButton(
            janela,
            bg_color = "#0F0F0F",
            fg_color = "#0F0F0F",
            text_color = "#4242E7",
            text = "Crie uma conta.",
            hover = None,
            font= ctk.CTkFont(
                "DejaVu Sans",
                12,
            ),
            command=lambda:criar_conta(janela)
        )
        botao_conta.place(
            x=245,
            y=370
        )

        #label é novo no pandora?
        texto_login_3 = ctk.CTkLabel(
            janela,
            bg_color = "#0F0F0F",
            text="É novo no Pandora?",
            font= ctk.CTkFont(
                "DejaVu Sans",
                12,
            )
        )
        texto_login_3.place(
            x=140,
            y=370
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
                janela.destroy()

                ctk.set_appearance_mode("dark")
                janela_sucesso_login = ctk.CTk()
                janela_sucesso_login.title("Sucesso")
                janela_sucesso_login.geometry("400x300")
                janela_sucesso_login.config(background="#0F0F0F")
                janela_sucesso_login.resizable(
                    width= False,
                    height= False
                )

                texto = ctk.CTkLabel(
                        janela_sucesso_login,
                        bg_color="#0F0F0F",
                        text="login realizado com sucesso!",
                        font=ctk.CTkFont(
                            "DejaVu Sans",
                            16,
                            "bold")
                )
                texto.pack(pady=40)

                botao_pandora= ctk.CTkButton(
                    janela_sucesso_login,
                    text= "Continuar",
                    command= lambda:pd_interface(janela_sucesso_login),
                    width= 210,
                    height= 45,
                    fg_color ="#3F812F",
                    hover_color="#356D28"
                )

                botao_pandora.pack(
                    pady= 0
                )

            else:
                erro = ctk.CTkLabel(
                janela,
                text="Usuário ou senha incorretos!",
                bg_color="#0F0F0F",
                text_color="red"
            )
            erro.place(x=170, y=420)

        #botao de entrar
        botao_entrar = ctk.CTkButton(
            janela,
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
            bg_color="#0F0F0F",
            fg_color ="#3F812F",
            hover_color = "#356D28",
        )
        botao_entrar.pack(
            pady=0
        )
        janela.mainloop()

        #função2
    #fim da função de trocar janela e criaçao da janela de login


    #janela 1 criação da janela continuar
    ctk.set_appearance_mode("dark")
    janela_1 = ctk.CTk()
    janela_1.title("Bem vindo ao Pandora")
    janela_1.geometry("520x560")
    janela_1.config(background="#0F0F0F")
    janela_1.resizable(
        width= False,
        height= False
    )

    texto_1 = ctk.CTkLabel(
        janela_1,
        text= "Bem vindo ao Pandora",
        bg_color="#0F0F0F",
        font = ctk.CTkFont(
            "DjaVu Sans",
            20,
            "bold"
        )
    )
    texto_1.pack(
        pady=80
    )

    #botao de entrar
    botao_continuar = ctk.CTkButton(
        janela_1,
        corner_radius=7,
        text_color= "#000000",
        text = "Continuar",
        font = ctk.CTkFont(
            "DjaVu Sans",
            12,
            "bold"
        ),
        width= 410,
        height= 45,
        bg_color="#0F0F0F",
        fg_color ="#FFFFFF",
        hover_color = "#B3B3B3",
        command=janela_de_login
    )
    botao_continuar.pack(
        pady=0
    )


    janela_1.mainloop()

