 #1-importando bibliotecas
import customtkinter as ctk
from customtkinter import *
from PIL import Image

def pd_interface(janela_sucesso_login):
    janela_sucesso_login.destroy()
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

    botao_home.pack(
        pady=10,
        anchor="w"

    )


    frame_4 = ctk.CTkFrame(
        janela,
        width= 1101,
        height= 768,
        corner_radius= 0,
        bg_color="#020202",
        fg_color="#020202",
        border_width=0.6,
        border_color="#060606"
    )

    frame_4.pack(
        side="top",
        fill = "y"
    )





    janela.mainloop()
