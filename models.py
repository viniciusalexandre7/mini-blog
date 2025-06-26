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