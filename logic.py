import database
from models import Usuario, Post

class Blog:
    def __init__(self):
        
        self.conn = database.conectar()
        database.criar_tabela_posts(self.conn)
        database.criar_tabela_usuarios(self.conn)
        
    def criar_usuario(self, nome, email):
        return database.inserir_usuario(self.conn, nome, email)
    
    def publicar_post(self, titulo, conteudo, email_usuario):
        return database.inserir_post(self.conn, titulo, conteudo, email_usuario)

    def listar_todos_os_post(self):
        posts_tuplas = database.buscar_todos_os_posts(self.conn)
        lista_de_objetos = []

        for tupla in posts_tuplas:
            post_obj = Post(post_id=tupla[0], titulo=tupla[1], conteudo=tupla[2], usuario_id=tupla[3], nome_autor=tupla[4])
            lista_de_objetos.append(post_obj)
        
        return lista_de_objetos

    def listar_post_por_id(self, post_id):
        tupla = database.buscar_post_por_id(self.conn, post_id)

        if tupla is not None:
                post_obj = Post(post_id=tupla[0], titulo=tupla[1], conteudo=tupla[2], usuario_id=tupla[3], nome_autor=tupla[4])
                return post_obj
        else:
            return None

    #possiveis atributos, nome, email, titulo
    def listar_post_por_atributo(self, atributo, valor_busca):
        post_tuplas = database.listar_post_por_atributo(self.conn, atributo, valor_busca)

        if not post_tuplas:
            return []

        if isinstance(post_tuplas, tuple):
           post_obj = Post(post_id=tupla[0], titulo=tupla[1], conteudo=tupla[2], usuario_id=tupla[3], nome_autor=tupla[4])
           return [post_obj]

        lista_de_objetos = []
        for tupla in post_tuplas:
            post_obj = Post(post_id=tupla[0], titulo=tupla[1], conteudo=tupla[2], usuario_id=tupla[3], nome_autor=tupla[4])
            lista_de_objetos.append(post_obj)
        
        return lista_de_objetos

    def atualizar_post(self, post_id, novo_titulo, novo_conteudo):
        return database.atualizar_post(self.conn, post_id, novo_titulo, novo_conteudo)

    def apagar_post(self, post_id):
        return database.apagar_post(self.conn, post_id)

    def listar_todos_os_usuarios(self):
        usuario_tupla = database.listar_todos_os_usuarios(self.conn)
        lista_de_usuarios = []
        for tupla in usuario_tupla:
            usuario_obj = Usuario(usuario_id=tupla[0], nome=tupla[1], email=tupla[2])
            lista_de_usuarios.append(usuario_obj)
        
        return lista_de_usuarios

    #possiveis atributos: nome, email
    def listar_usuarios_por_atributo(self, atributo, valor_busca):
        usuario_tupla = database.listar_usuario_por_atributo(self.conn, atributo, valor_busca)

        if not usuario_tupla:
            return []

        if isinstance(usuario_tupla, tuple):
            usuario_obj = Usuario(usuario_id=usuario_tupla[0], nome=usuario_tupla[1], email=usuario_tupla[2])
            return [usuario_obj]

        lista_de_usuarios = []
        for tupla in usuario_tupla:
            usuario_obj = Usuario(usuario_id=tupla[0], nome=tupla[1], email=tupla[2])
            lista_de_usuarios.append(usuario_obj)
        
        return lista_de_usuarios

    def deletar_usuario(self, email):
        return database.deletar_usuario(self.conn, email)

    def atualizar_usuario(self, email_buscado, novo_nome, novo_email):
        return database.atualizar_usuario(self.conn, email_buscado, novo_nome, novo_email)

    def fechar_conexao(self):
        fechar = self.conn.close()
        return fechar