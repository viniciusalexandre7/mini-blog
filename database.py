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

        cursor.execute("SELECT 1 FROM usuarios WHERE email = ?", (email,))
        usuario_existe = cursor.fetchone()

        if usuario_existe is None:
            cursor.execute("""INSERT INTO usuarios (nome, email) VALUES (?, ?)""", (nome, email))
            conn.commit()
            print(f"Usuario '{nome}' adicionado com sucesso!")
            return cursor.lastrowid

        else:
            print("E-mail já cadastrado. Escolha outro.")
            return None

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

def buscar_todos_os_posts(conn):

    try:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT posts.id, posts.titulo, posts.conteudo, usuarios.nome FROM posts
        JOIN usuarios ON posts.usuario_id = usuarios.id
        ;
        """)
        posts = cursor.fetchall()
        return posts

    except sqlite3.Error as error:
        print(f"Erro ao buscar posts: {error}")
        return []

def buscar_post_por_id(conn, post_id):

    try: 
        cursor = conn.cursor() 
        cursor.execute("""
        SELECT posts.titulo, posts.conteudo, usuarios.nome
        FROM posts
        JOIN usuarios ON posts.usuario_id = usuarios.id
        WHERE posts.id = ?
        """,(post_id),) 

        posts = cursor.fetchall() 
        return posts 

    except sqlite3.Error as error: 
        print(f"Erro ao buscar posts: {error}") 
        return []


def atualizar_post(conn, post_id, novo_titulo, novo_conteudo):

    try:
        cursor = conn.cursor()

        if not novo_titulo.strip() or not novo_conteudo.strip():
            print("Título e conteúdo não podem ser vazios.")
            return

        cursor.execute("SELECT 1 FROM posts WHERE id = ?", (post_id,))
        if cursor.fetchone() is None:
            print(f"Nenhum post encontrado com ID {post_id}.")
            return

        cursor.execute("""UPDATE posts SET titulo = ?, conteudo = ? WHERE id = ?""", (novo_titulo, novo_conteudo, post_id,))

        conn.commit()
        print(f"Post com ID {post_id} atualizado com sucesso!")

    except sqlite3.Error as error:
        print(f"Erro ao atualizar post: {error}")

def listar_todos_os_usuarios(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT nome, email From usuarios
        """)
        usuarios = cursor.fetchall()
        return usuarios

    except sqlite3.Error as error:
        print(f"Erro ao buscar usuarios: {error}")
        return []

def listar_usuario_por_email(conn, email):

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
        usuario = cursor.fetchone()
        return usuario

    except sqlite3.Error as error:
        print(f"Erro ao buscar usuarios: {error}")
        return []

def deletar_usuario(conn, email):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
        resultado = cursor.fetchone()

        if resultado:
            usuario_id = resultado[0]
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
            conn.commit()

            if cursor.rowcount:
                print(f"usuario com deletado com sucesso!")
            else:
                print(f"Falha ao deletar o usuário.")
                
        else:
            print(f"Nenhum usuario encontrado com o email: '{email}'.")

    except sqlite3.Error as error:
        print(f"Erro ao deletar usuario {error} ")

def atualizar_usuario(conn, email_buscado, novo_nome, novo_email):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email_buscado,))
        resultado = cursor.fetchone()

        if resultado:
            usuario_id = resultado[0]
            cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, usuario_id,))
            conn.commit()

            if cursor.rowcount:
                print(f"usuario atualizado com sucesso!")
            else:
                print(f"Falha ao atualizar o usuário.")
        else:
            print(f"Nenhum usuario encontrado com o email: '{email_buscado}'.")

    except sqlite3.Error as error:
        print(f"Erro ao atualizar usuario {error} ")



def apagar_post(conn, post_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        conn.commit()

        if cursor.rowcount:
            print(f"Post com ID '{post_id}' deletado com sucesso!")
        else:
            print(f"Nenhum post encontrado com o ID '{post_id}'.")

    except sqlite3.Error as error:
        print(f"Erro ao apagar post {error} ")

if __name__ == "__main__":

    conexao = conectar()

    if conexao:
        # criar_tabela_usuarios(conexao)
        # criar_tabela_posts(conexao)
        # inserir_usuario(conexao, "vinicius", "vini123@gmail.com")
        # inserir_usuario(conexao, "ana", "ana123@gmail.com")
        # inserir_post(conexao, "Dicassad de Treino", "dicasdas", "ana12s3@gmail.com")
        # atualizar_status(conexao, 4, "testando")
        apagar_post(conexao, 3)

        # posts = buscar_post_por_id(conexao, "1")
        # print("\nLista de Posts:")
        # for conteudo, titulo, nome in posts:
        #     print(f"{conteudo} - {titulo} - {nome}")
        # for id, titulo, conteudo, id_usuario in posts:
        #     print(f"id_post: {id} - titulo: {titulo} - conteudo: {conteudo} - id_usuario: {id_usuario}")
        
        conexao.close()
        print("Conexão fechada.")