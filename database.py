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

    except sqlite3.Error as error:
        print(f"Erro ao criar tabela: {error}")


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

    except sqlite3.Error as error:
        print(f"Erro ao criar tabela: {error}")

def inserir_usuario(conn, nome, email):

    try:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO usuarios (nome, email) VALUES (?, ?)""", (nome, email))
        conn.commit()
        print(f"Usuario '{nome}' adicionado com sucesso!")

    except sqlite3.Error as error:
        print(f"Erro ao inserir usuario: {error}")
        return None

def inserir_post(conn, titulo, conteudo, email_usuario):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email_usuario,))
        resultado = cursor.fetchone()

        if resultado:
            usuario_id = resultado[0]
            cursor.execute("""INSERT INTO posts (titulo, conteudo, usuario_id) VALUES (?, ?, ?)""", (titulo, conteudo, usuario_id))
            conn.commit()
            print(f"{titulo} foi postado com sucesso!")

        else:
             print("Usuário não encontrado, não foi possível inserir o post.")

    except sqlite3.Error as error:
        print(f"Erro ao inserir post: {error}")






if __name__ == "__main__":

    conexao = conectar()

    if conexao:
        # criar_tabela_usuarios(conexao)
        # criar_tabela_posts(conexao)
        # inserir_usuario(conexao, "vinicius", "vini123@gmail.com")
        # inserir_usuario(conexao, "ana", "ana123@gmail.com")
        inserir_post(conexao, "Dicassad de Treino", "dicasdas", "ana12s3@gmail.com")
        # atualizar_status(conexao, 4, "testando")
        # deletar_tarefa(conexao, 5)

        # tarefas = buscar_todas_tarefas(conexao)
        # print("\nLista de Tarefas:")
        # for id, descricao, status in tarefas:
        #     print(f"{id}. {descricao} - Status: {status}")
        
        conexao.close()
        print("Conexão fechada.")