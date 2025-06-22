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
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
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
            return cursor.lastrowid
        else:
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
            return cursor.rowcount  

        else:
             return 0

    except sqlite3.Error as error:
        print(f"Erro ao inserir post: {error}")
        return 0

def buscar_todos_os_posts(conn):

    try:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT posts.id, posts.titulo, posts.conteudo, posts.usuario_id, usuarios.nome FROM posts
        JOIN usuarios ON posts.usuario_id = usuarios.id
        ;
        """)
        posts = cursor.fetchall()
        return posts

    except sqlite3.Error as error:
        print(f"Erro ao buscar posts: {error}")
        return []


def listar_post_por_atributo(conn, atributo, valor_busca):
    
    try:
        atributos_permitidos = ["email", "nome", "titulo"]

        if atributo not in atributos_permitidos:
            return 0

        cursor = conn.cursor()

        if atributo in ['nome', 'email']:
            campo_tabela = f"usuarios.{atributo}"
        else:
            campo_tabela = f"posts.{atributo}"
    
        cursor.execute(f"""
        SELECT posts.id, posts.titulo, posts.conteudo, posts.usuario_id, usuarios.nome
        FROM posts
        JOIN usuarios ON posts.usuario_id = usuarios.id
        WHERE {campo_tabela} = ?
        """, (valor_busca,))
        return cursor.fetchall()

    except sqlite3.Error as error:
        print(f"Erro ao buscar posts: {error}")
        return []


def buscar_post_por_id(conn, post_id):

    try: 
        cursor = conn.cursor() 
        cursor.execute("""
        SELECT posts.id, posts.titulo, posts.conteudo, posts.usuario_id, usuarios.nome 
        FROM posts
        JOIN usuarios ON posts.usuario_id = usuarios.id
        WHERE posts.id = ?
        """,(post_id),) 

        posts = cursor.fetchone() 
        return posts 

    except sqlite3.Error as error: 
        print(f"Erro ao buscar posts: {error}") 
        return None


def atualizar_post(conn, post_id, novo_titulo, novo_conteudo):

    try:
        cursor = conn.cursor()
        cursor.execute("""UPDATE posts SET titulo = ?, conteudo = ? WHERE id = ?""", (novo_titulo, novo_conteudo, post_id,))
        conn.commit()
        return cursor.rowcount  

    except sqlite3.Error as error:
        print(f"Erro ao atualizar post: {error}")
        return 0

def apagar_post(conn, post_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        conn.commit()
        return cursor.rowcount  

    except sqlite3.Error as error:
        print(f"Erro ao apagar post {error} ")
        return 0

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

def listar_usuario_por_atributo(conn, atributo, valor_busca):
    try:
        atributos_permitidos = ["email", "nome"]

        if atributo not in atributos_permitidos:
            return 0

        cursor = conn.cursor()

        cursor.execute(f"""
        SELECT id, nome, email FROM usuarios WHERE {atributo} = ?
        """, (valor_busca,))

        return cursor.fetchone() if atributo == "email" else cursor.fetchall()

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
            return cursor.rowcount         
        else:
            return 0

    except sqlite3.Error as error:
        print(f"Erro ao deletar o usuário com e-mail {email}: {error}")
        return 0

def atualizar_usuario(conn, email_buscado, novo_nome, novo_email):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email_buscado,))
        resultado = cursor.fetchone()

        if resultado:
            usuario_id = resultado[0]
            cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, usuario_id,))
            conn.commit()
            return cursor.rowcount  
        else:
            return 0

    except sqlite3.Error as error:
        print(f"Erro ao atualizar usuario {error} ")
        return 0


if __name__ == "__main__":

    conexao = conectar()

    if conexao:
        # criar_tabela_usuarios(conexao)
        # criar_tabela_posts(conexao)
        # inserir_usuario(conexao, "vinicius", "vini123@gmail.com")
        # inserir_usuario(conexao, "ana", "ana123@gmail.com")
        print(inserir_post(conexao, "Dicassad de Treino", "dicasdas", "ana123@gmail.com"))
        # atualizar_status(conexao, 4, "testando")
        # apagar_post(conexao, 3)

        # posts = buscar_post_por_id(conexao, "1")
        # print("\nLista de Posts:")
        # for conteudo, titulo, nome in posts:
        #     print(f"{conteudo} - {titulo} - {nome}")
        # for id, titulo, conteudo, id_usuario in posts:
        #     print(f"id_post: {id} - titulo: {titulo} - conteudo: {conteudo} - id_usuario: {id_usuario}")
        
        conexao.close()
        print("Conexão fechada.")