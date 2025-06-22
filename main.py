import database
import os

class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"ID:{id} - Nome: {self.nome} - Email: {self.email}"
    
        
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
        
