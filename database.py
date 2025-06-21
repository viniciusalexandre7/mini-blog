import sqlite3

def conectar():
    conn = sqlite3.connect('blog.db')
    return conn

def criar_tabela(conn):

    try:
        cursor = conn.cursor()

    except sqlite3.Error as e:
        print(f"Erro de {e}")