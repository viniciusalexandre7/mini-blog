import database
import os

class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome} - Email: {self.email}"
    
        
class Post:
    def __init__(self, id, titulo, conteudo, usuario_id, nome_autor):
        self.id = id
        self.titulo = titulo
        self.conteudo = conteudo
        self.usuario_id = usuario_id
        self.nome_autor = nome_autor

    def __str__(self):
        return f"ID: {self.id} - Título: {self.titulo} - Conteudo: {self.conteudo} - ID_Usuario: {self.usuario_id} - Nome do autor: {self.nome_autor}"

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

    def fechar_conexao(self):
        fechar = self.conn.close()
        return fechar



