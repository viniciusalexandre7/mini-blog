import sqlite3

def conectar():
    conn = sqlite3.connect('blog.db')
    return conn

def criar_tabela_usuarios(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT UNIQUE
            );
        """)
        conn.commit()

    except sqlite3.Error as e:
        print(f"Erro ao criar tabela: {e}")


def criar_tabela_posts(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            titulo TEXT,
            conteudo TEXT,
            usuario_id INTEGER,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            );
        """)
        conn.commit()

    except sqlite3.Error as e:
        print(f"Erro ao criar tabela: {e}")
