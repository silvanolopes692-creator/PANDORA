import sqlite3 
from sqlite3 import *

def banco_de_dados():
    conexao = sqlite3.connect("pd_login.db")
    cursor = conexao.cursor()

    comando_SQL = """
    CREATE TABLE IF NOT EXISTS usuarios(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME TEXT UNIQUE NOT NULL,
        EMAIL TEXT UNIQUE NOT NULL,
        SENHA TEXT NOT NULL
    )
    """
    cursor.execute(comando_SQL)
    conexao.commit()
    conexao.close()

    print("banco de dados criado com sucesso!")

