 #1-importando bibliotecas
import customtkinter as ctk
from customtkinter import *
from PIL import Image

def pd_interface(janela_2):
    janela_2.destroy()
    #2-tema escuro
    ctk.set_appearance_mode("dark")

    #3-defenir cor padrão
    ctk.set_default_color_theme("dark-blue")

    #4-criação e resolução da janela e titutlo
    janela = ctk.CTk()
    janela.geometry("1366x768")
    janela.config(background="#020202")
    janela.resizable(
        width= True,
        height= True
    )
    janela.title("Pandora")


    frame_1 = ctk.CTkFrame(
        janela,
        width= 250,
        corner_radius= 0,
        bg_color="#020202",
        fg_color="#020202",
        border_width=0.6,
        border_color="#2A2A2A"
    )

    frame_1.pack(
        side="left",
        fill="y"
    )


    frame_2 = ctk.CTkFrame(
        frame_1,
        width= 250,
        height= 70,
        corner_radius= 0,
        bg_color="#020202",
        fg_color="#020202",
        border_width=0.6,
        border_color="#2A2A2A"
    )

    frame_2.pack(
        side="bottom",
    )

    frame_3 = ctk.CTkFrame(
        janela,
        width= 1366,
        height= 55,
        corner_radius= 0,
        bg_color="#020202",
        fg_color="#020202",
        border_width=0.6,
        border_color="#050505"
    )

    frame_3.pack(
        side="top",
        fill = "x"
    )


    logo = ctk.CTkImage(
        Image.open("imagens/pandora_3.jpg"),
        size= (35,30)
    )

    botao_home = ctk.CTkButton(
        frame_1,
        bg_color="#020202",
        fg_color="#020202",
        corner_radius=35,
        hover_color="#020202",
        image= logo,
        text="Inicio", 
        font= ctk.CTkFont(
                    "DejaVu Sans",
                    13,
                    "bold"
        ),
        width=0,
        height=50
    )

    botao_home.place(
        x=2,
        y=10

    )


    frame_4 = ctk.CTkFrame(
        janela,
        width= 1101,
        height= 768,
        corner_radius= 0,
        bg_color="#000000",
        fg_color="#000000",
        border_width=0.6,
        border_color="#060606"
    )

    frame_4.pack(
        side="top",
        fill = "y"
    )



    logo_1 = ctk.CTkImage(
        Image.open("imagens/pandora_1.png"),
        size= (80,80)
    )

    botao_home_1= ctk.CTkButton(
        frame_4,
        bg_color="#000000",
        fg_color="#000000",
        corner_radius=35,
        hover_color="#000000",
        image= logo_1,
        text="Pandora", 
        font= ctk.CTkFont(
                    "DejaVu Sans",
                    30,
                    "bold"
        ),
        width=400,
        height=200
    )

    botao_home_1.place(
        x=280,
        y=30

    )


    caixa_1 = ctk.CTkButton(
        frame_4,
        width=160,
        height=100,
        text="Pesquisar",
        bg_color="#000000",
        hover_color="#000000",
        fg_color="#1A4700",
        corner_radius=17,
        border_width=2,
        border_color="#3CFF00",
        font= ctk.CTkFont(
                    "DejaVu Sans",
                    20,
                    "bold"
        ),
    )
    caixa_1.place(
        x=220,
        y=210
    )


    caixa_2 = ctk.CTkButton(
        frame_4,
        width=160,
        height=100,
        text="Exame",
        bg_color="#000000",
        hover_color="#000000",
        fg_color="#39003B",
        corner_radius=17,
        border_width=2,
        border_color="#F700FF",
        font= ctk.CTkFont(
                    "DejaVu Sans",
                    20,
                    "bold"
        ),
    )
    caixa_2.place(
        x=420,
        y=210
    )



    caixa_3 = ctk.CTkButton(
        frame_4,
        width=160,
        height=100,
        text="Teoria",
        bg_color="#000000",
        hover_color="#000000",
        fg_color="#000436",
        corner_radius=17,
        border_width=2,
        border_color="#0919FD",
        font= ctk.CTkFont(
                    "DejaVu Sans",
                    20,
                    "bold"
        ),
    )
    caixa_3.place(
        x=620,
        y=210
    )



    caixa_4 = ctk.CTkButton(
        frame_4,
        width=160,
        height=100,
        text="Estudar",
        bg_color="#000000",
        hover_color="#000000",
        fg_color="#680000",
        corner_radius=17,
        border_width=2,
        border_color="#FF0000",
        font= ctk.CTkFont(
                    "DejaVu Sans",
                    20,
                    "bold"
        ),
    )
    caixa_4.place(
        x=320,
        y=350
    )


    caixa_5 = ctk.CTkButton(
        frame_4,
        width=160,
        height=100,
        text="Cursos",
        bg_color="#000000",
        hover_color="#000000",
        fg_color="#00684E",
        corner_radius=17,
        border_width=2,
        border_color="#00FFD5",
        font= ctk.CTkFont(
                    "DejaVu Sans",
                    20,
                    "bold"
        ),
    )
    caixa_5.place(
        x=520,
        y=350
    )


    perfil = ctk.CTkButton(
        frame_2,
        width= 40,
        corner_radius= 20,
        height=40,
        text=None,
        bg_color="#020202",
        fg_color="#414141"
    )
    perfil.place(
        x=15,
        y=15
    )

    texto_perfil = ctk.CTkLabel(
        frame_2,
        text="Fazer Login",
        font= ctk.CTkFont(
            "DejaVu Sans",
            13,
            "bold"
        )
    )
    texto_perfil.place(
        x=67,
        y=21
    )

    versao = ctk.CTkLabel(
        frame_4,
        text="Versão 1.0.0 ",
        font=ctk.CTkFont(
            "DejaVu Sans",
            13
        )
    )
    versao.place(
        x=1000,
        y=610
    )


    pesquisa = ctk.CTkEntry(
        frame_3,
        bg_color="#020202",
        fg_color="#020202",
        width= 900,
        height= 45,
        corner_radius=8,
        border_width=1,
        border_color="#2A2A2A",
        placeholder_text="Pesquisar..."
    )
    pesquisa.place(
        x=95,
        y=5
    )




    janela.mainloop()
