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

def gerenciar_listagem_de_todos_os_posts(blog_obj):
    lista_de_post = blog_obj.listar_todos_os_post()

    if not lista_de_post:
        print("Não há posts para serem listados")
        return
   
    for indice, post in enumerate(lista_de_post, start=1):
        print(f"{indice}. {post.titulo} por {post.nome_autor}")


def gerenciar_listagem_de_post_por_id(blog_obj, post_id):
    post = blog_obj.listar_post_por_id(post_id)

    if not post:
        print(f"Não há nenhum post com o ID: {post_id}.")
        return

    print(f"{post.titulo} por {post.nome_autor}")
    print(f"\nConteúdo:\n{post.conteudo}")


def gerenciar_listagem_por_atributo(blog_obj, atributo, valor_busca):
    lista_de_post = blog_obj.listar_post_por_atributo(atributo, valor_busca)

    if not lista_de_post:
        print(f"Não há posts com o {atributo}: {valor_busca}.")
        return 

    for indice, post in enumerate(lista_de_post, start=1):
        print(f"{indice}. {post.titulo} por {post.nome_autor}")

def gerenciar_acao_post(blog_obj, post_id):
    post = blog_obj.listar_post_por_id(post_id)
    if not post:
        print(f"Post com ID {post_id} não foi encontrado.")
        return
    
    print(f"\nPost selecionado: '{post.titulo}' por {post.nome_autor}\n")
    print("O que deseja fazer com esse post?")
    print("1. Atualizar")
    print("2. Apagar")
    print("3. Cancelar")

    try:
        escolha = int(input("Digite o número da ação desejada: ").strip())
        if escolha == 1:
            novo_titulo = input("Novo título: ").strip()
            novo_conteudo = input("Novo conteúdo: ").strip()
            resultado = blog_obj.atualizar_post(post_id, novo_titulo, novo_conteudo)

            if resultado is None:
                print("Erro ao tentar atualizar o post.")
            elif resultado == 0:
                print("Nenhum post foi atualizado.")
            else:
                print(f"Post com ID {post_id} atualizado com sucesso!")

        elif escolha == 2:
            confirmar = input("Tem certeza que deseja apagar este post? (s/n): ").strip().lower()
            if confirmar == "s":
                resultado = blog_obj.apagar_post(post_id)
                if resultado is None:
                    print("Erro ao tentar apagar o post.")
                elif resultado == 0:
                    print("Nenhum post foi apagado.")
                else:
                    print(f"Post com ID {post_id} apagado com sucesso!")
            else:
                print("Ação de exclusão cancelada.")

        elif escolha == 3:
            print("Ação cancelada.")
            return

        else:
            print("Opção inválida.")
            return

    except ValueError:
        print("Digite um valor númerico")
        return
