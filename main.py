from models import Usuario, Post
from logic import Blog


def gerenciar_criacao_usuario(blog_obj, nome, email):
    if blog_obj.criar_usuario(nome, email) is not None:
        print(f"Usuario {nome} criado com sucesso!")
    else:
        print(f"erro ao criar o usuario {nome}")

def gerenciar_criacao_de_post(blog_obj, titulo, conteudo, email_usuario):
    titulo = titulo.strip()
    conteudo = conteudo.strip()
    email_usuario = email_usuario.strip().lower()
    usuario = blog_obj.listar_usuarios_por_atributo("email", email_usuario)
    nome_usuario = usuario[1] if usuario else None

    post_id = blog_obj.publicar_post(titulo, conteudo, email_usuario)

    if post_id:
        print(f"Post criado com sucesso pelo usuário {nome_usuario or 'desconhecido'}! ID: {post_id}")
    else:
        print(f"Erro ao criar o post para o usuário {nome_usuario or email_usuario}")

def gerenciar_listagem_de_todos_os_posts():
    
    
