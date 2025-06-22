import database
import os

class Usuario:
    def __init__(self, usuario_id, nome, email):
        self.usuario_id = usuario_id
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome} - Email: {self.email}"
    
        
class Post:
    def __init__(self, post_id, titulo, conteudo, usuario_id, nome_autor):
        self.post_id = post_id
        self.titulo = titulo
        self.conteudo = conteudo
        self.usuario_id = usuario_id
        self.nome_autor = nome_autor

    def __str__(self):
        return f"ID: {self.post_id} - Título: {self.titulo} - Conteudo: {self.conteudo} - ID_Usuario: {self.usuario_id} - Nome do autor: {self.nome_autor}"

class Blog:
    def __init__(self):
        
        self.conn = database.conectar()
        database.criar_tabela_posts(self.conn)
        database.criar_tabela_usuarios(self.conn)
        
    def criar_usuario(self, nome, email):
        database.inserir_usuario(self.conn, nome, email)
    
    def publicar_post(self, titulo, conteudo, email_usuario):
        database.inserir_post(self.conn, titulo, conteudo, email_usuario)

    def listar_todos_os_post(self):
        posts_tuplas = database.buscar_todos_os_posts(self.conn)
        lista_de_objetos = []

        for tupla in posts_tuplas:
            post_obj = Post(id=tupla[0], titulo=tupla[1], conteudo=tupla[2], usuario_id=tupla[3], nome_autor=tupla[4])
            lista_de_objetos.append(post_obj)
        
        return lista_de_objetos

    def listar_post_por_id(self, post_id):
        tupla = database.buscar_post_por_id(self.conn, post_id)

        if tupla is not None:
                post_obj = Post(id=tupla[0], titulo=tupla[1], conteudo=tupla[2], usuario_id=tupla[3], nome_autor=tupla[4])
                return post_obj
        else:
            return None

    #possiveis atributos, nome, email, titulo
    def listar_post_por_atributo(self, atributo, valor_busca):
        post_tuplas = database.listar_post_por_atributo(self.conn, atributo, valor_busca)
        lista_de_objetos = []

        for tupla in post_tuplas:
            post_obj = Post(id=tupla[0], titulo=tupla[1], conteudo=tupla[2], usuario_id=tupla[3], nome_autor=tupla[4])
            lista_de_objetos.append(post_obj)
        
        return lista_de_objetos

    def atualizar_post(self, post_id, novo_titulo, novo_conteudo):
        database.atualizar_post(self.conn, post_id, novo_titulo, novo_conteudo)

    def apagar_post(self, post_id):
        database.apagar_post(self.conn, post_id)

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

        if isinstance(usuario_tupla, tuple):
            return Usuario(usuario_id=usuario_tupla[0], nome=usuario_tupla[1], email=usuario_tupla[2])


        lista_de_usuarios = []
        for tupla in usuario_tupla:
            usuario_obj = Usuario(usuario_id=tupla[0], nome=tupla[1], email=tupla[2])
            lista_de_usuarios.append(usuario_obj)
        
        return lista_de_usuarios

    def deletar_usuario(self, email):
        database.deletar_usuario(self.conn, email)

    def atualizar_usuario(self, email_buscado, novo_nome, novo_email):
        database.atualizar_usuario(self.conn, email_buscado, novo_nome, novo_email)


    def fechar_conexao(self):
        fechar = self.conn.close()
        return fechar



