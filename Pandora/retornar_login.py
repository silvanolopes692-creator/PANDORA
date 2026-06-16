from customtkinter import *
import customtkinter as ctk
import sqlite3

def janela_de_login_1(janela_sucesso,):
        janela_sucesso.destroy()
        from pd_interface import pd_interface
        from pd_criar_conta import criar_conta

        #criação da janelafazer login
        ctk.set_appearance_mode("dark")
        janela_3 = ctk.CTk()
        janela_3.title("Faça login no Pandora")
        janela_3.geometry("520x560")
        janela_3.config(background="#020202")
        janela_3.resizable(
            width= False,
            height= False
        )

        #inicio da janela fazer login
        # 
        # 
        #  
        #label de texto login
        texto_login = ctk.CTkLabel(
            janela_3,
            text= "Faça login no Pandora",
            bg_color="#020202",
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
            janela_3,
            text= "Nome de usuário ou endereço de e-mail",
            bg_color="#020202",
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
            janela_3,
            corner_radius=10,
            width= 410,
            height= 45,
            bg_color="#020202",
            fg_color="#020202"
        )
        caixa_de_nome.pack(
            pady= 0
        )
        #label DE TEXTO DE SENHA
        texto_login_2 = ctk.CTkLabel(
            janela_3,
            text= "Senha",
            bg_color="#020202",
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
            janela_3,
            show = "*",
            corner_radius=10,
            width= 410,
            height= 45,
            bg_color="#020202",
            fg_color="#020202"
        )
        caixa_de_nome_1.pack(
            pady= 40
        )

        #botão criar uma conta
        botao_conta = ctk.CTkButton(
            janela_3,
            bg_color = "#020202",
            fg_color = "#020202",
            text_color = "#4242E7",
            text = "Crie uma conta.",
            hover = None,
            font= ctk.CTkFont(
                "DejaVu Sans",
                12,
            ),
            command=lambda:criar_conta(janela_3)
        )
        botao_conta.place(
            x=245,
            y=370
        )

        #label é novo no pandora?
        texto_login_3 = ctk.CTkLabel(
            janela_3,
            bg_color = "#020202",
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
                janela_3.destroy()

                ctk.set_appearance_mode("dark")
                janela_sucesso_login = ctk.CTk()
                janela_sucesso_login.title("Sucesso")
                janela_sucesso_login.geometry("400x300")
                janela_sucesso_login.config(background="#020202")
                janela_sucesso_login.resizable(
                    width= False,
                    height= False
                )

                texto = ctk.CTkLabel(
                        janela_sucesso_login,
                        bg_color="#020202",
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
                janela_3,
                text="Usuário ou senha incorretos!",
                bg_color="#020202",
                text_color="red"
            )
            erro.place(x=170, y=420)

        #botao de entrar
        botao_entrar = ctk.CTkButton(
            janela_3,
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
            bg_color="#020202",
            fg_color ="#3F812F",
            hover_color = "#356D28",
        )
        botao_entrar.pack(
            pady=0
        )
        janela_3.mainloop()
