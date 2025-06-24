from models import Usuario, Post
from logic import Blog
import os



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
    nome_usuario = usuario.nome if usuario else None

    post_id = blog_obj.publicar_post(titulo, conteudo, email_usuario)

    if post_id:
        print(f"Post criado com sucesso pelo usuário {nome_usuario or 'desconhecido'}! O post obteve o ID: {post_id}")
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

def gerenciar_listagem_de_post_por_atributo(blog_obj, atributo, valor_busca):
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

def gerenciar_listagem_de_usuarios(blog_obj):

    lista_de_usuarios = blog_obj.listar_todos_os_usuarios()

    if not lista_de_usuarios:
        print("Não há usuarios para serem listados")
        return
   
    for indice, usuario in enumerate(lista_de_usuarios, start=1):
        print(f"{indice}. {usuario.nome} - {usuario.email}")

def gerenciar_listagem_de_usuario_por_atributo(blog_obj, atributo, valor_busca):
    lista_de_usuarios = blog_obj.listar_usuarios_por_atributo(atributo, valor_busca)

    if not lista_de_usuarios:
        print(f"Não há usuarios com o {atributo}: {valor_busca}.")
        return 

    for indice, usuario in enumerate(lista_de_usuarios, start=1):
        print(f"{indice}. {usuario.nome} - {usuario.email}")


def gerenciar_acao_usuario(blog_obj, email_usuario):

    usuarios = blog_obj.listar_usuarios_por_atributo("email", email_usuario)

    if not usuarios:
        print(f"{email_usuario} não foi encontrado!")
        return

    usuario = usuarios[0]

    print(f"\nUsuario selecionado: '{usuario.nome}' - {usuario.email}\n")
    print("O que deseja fazer com esse usuario?")
    print("1. Atualizar")
    print("2. Apagar")
    print("3. Cancelar")

    try:
        escolha = int(input("Digite o número da ação desejada: ").strip())
        if escolha == 1:
            novo_nome = input("Novo nome: ").strip()
            novo_email = input("Novo email: ").strip()
            resultado = blog_obj.atualizar_usuario(email_usuario, novo_nome, novo_email)

            if resultado is None:
                print("Erro ao tentar atualizar o usuario.")
            elif resultado == 0:
                print("O usuario não foi atualizado.")
            else:
                print(f"Usuario com email {email_usuario} atualizado com sucesso!")

        elif escolha == 2:
            confirmar = input("Tem certeza que deseja apagar este usuario? (s/n): ").strip().lower()
            if confirmar == "s":
                resultado = blog_obj.deletar_usuario(email_usuario)
                if resultado is None:
                    print("Erro ao tentar apagar o usuario.")
                elif resultado == 0:
                    print("O usuario não foi apagado.")
                else:
                    print(f"Usuario com o email:{email_usuario} apagado com sucesso!")
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


#INTERFACE

def main():

    blog = Blog()

    while True:

        print("\n==== MENU DO BLOG ====")
        print("1. Adicionar Usuario")
        print("2. Adicionar Post")
        print("3. Listar todos os post")
        print("4. Listar post por Atributo")
        print("5. Gerenciar ação do post (Atualizar ou Deletar)")
        print("6. Listar todos os usuarios")
        print("7. Listar usuario por atributo")
        print("8. Gerenciar ação do usuario (Atualizar ou Deletar)")
        print("0. Sair")


        try:
            escolha = int(input("Digite a opção: ").strip())

            if escolha == 1:
                os.system("cls")
                print("---ADICIONAR NOVO USUARIO---")
                nome = input("Digite o seu nome: ").strip().lower()
                email = input("Digite o seu email: ").strip().lower()
                gerenciar_criacao_usuario(blog, nome, email)

            elif escolha == 2:
                os.system("cls")
                print("---ADICIONAR NOVO POST---")
                email_usuario = input("Digite o seu email: ").strip().lower()

                usuario_existe = blog.listar_usuarios_por_atributo("email", email_usuario)
                if usuario_existe:
                    titulo = input("Digite o titulo do seu post: ").strip().lower()
                    conteudo = input("Escreva sobre oq você irá dizer: ").strip().lower()
                    gerenciar_criacao_de_post(blog, titulo, conteudo, email_usuario)
                else:
                    print("O email digitado não pertence a nenhum usuario!")

            elif escolha == 3:
                os.system("cls")
                print("---LISTAR POSTS---") 
                gerenciar_listagem_de_todos_os_posts(blog)

            elif escolha == 4:
                os.system("cls")
                print("---LISTAR POSTS POR ATRIBUTOS---") 
                print("Escolha o atributo que deseja buscar")
                print("1- Titulo do post\n2- Nome do autor\n3- Email do autor\n0- Sair")
                try:
                    escolha = int(input("Selecione a opção: "))
                    if escolha == 1:
                        atributo = "titulo"
                        valor_busca = input("Digite o titulo que deseja buscar: ").strip().lower()
                        gerenciar_listagem_de_post_por_atributo(blog, atributo, valor_busca)

                    elif escolha == 2:
                        atributo = "nome"
                        valor_busca = input("Digite o nome do autor que deseja buscar: ").strip().lower()
                        gerenciar_listagem_de_post_por_atributo(blog, atributo, valor_busca)
                        
                    elif escolha == 3:
                        atributo = "email"
                        valor_busca = input("Digite o email do autor que deseja buscar: ").strip().lower()
                        gerenciar_listagem_de_post_por_atributo(blog, atributo, valor_busca)

                    elif escolha == 0:
                        print("Operação cancelada")

                    else:
                        print("Digite uma opção válida")
                    
                except ValueError:
                    print("Digite um valor numerico")
            
            elif escolha == 5:
                os.system("cls")
                print("---AÇÕES DO POST---") 
                post_id = input("Digite o ID do post que você deseja alterar: ")
                gerenciar_acao_post(blog, post_id)


            elif escolha == 6:
                os.system("cls")
                print("---LISTAR TODOS OS USUARIOS---") 
                gerenciar_listagem_de_usuarios(blog)

            
            elif escolha == 7:
                os.system("cls")
                print("---LISTAR TODOS OS USUARIOS POR ATRIBUTO---") 
                print("Escolha o atributo que deseja buscar")
                print("1- Nome do usuario\n2- Email do usuario\n0- Sair")

                try:
                    escolha = int(input("Selecione a opção: "))
                    if escolha == 1:
                        atributo = "nome"
                        valor_busca = input("Digite o nome que deseja buscar: ").strip().lower()
                        gerenciar_listagem_de_usuario_por_atributo(blog, atributo, valor_busca)

                    elif escolha == 2:
                        atributo = "email"
                        valor_busca = input("Digite o email que deseja buscar: ").strip().lower()
                        gerenciar_listagem_de_usuario_por_atributo(blog, atributo, valor_busca)  

                    elif escolha == 0:
                        print("Operação cancelada")                       

                    else:
                        print("Digite uma opção válida")
                    
                except ValueError:
                    print("Digite um valor numerico")

            elif escolha == 8:
                os.system("cls")
                print("---AÇÕES DO USUARIO---") 
                email_usuario = input("Digite o email do usuario que você deseja fazer alterarações: ")
                gerenciar_acao_usuario(blog, email_usuario)

            elif escolha == 0:
                print("Saindo do programa...")
                blog.fechar_conexao()
                break

            else:
                 print("Opção inválida, tente novamente!")
            
        except ValueError:
            print("Digite um valor númerico")



if __name__ == "__main__":
    main()