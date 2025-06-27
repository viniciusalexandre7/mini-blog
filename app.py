from flask import Flask, request
from logic import Blog
from models import Post, Usuario

app = Flask(__name__)

blog = Blog()

@app.route('/')
def pagina_inicial():
    return """
    <h1>Página Inicial do Blog</h1>
    <a href='/post'>Ver todos os posts</a>
    <br> <a href='/registrar'>Criar um usuario</a>
    <br> <a href='/registrar_post'>Criar um post</a>
    """

@app.route('/registrar', methods =['GET', 'POST'])
def registrar_usuario():
    print("✅ Rota /registrar acessada")
    if request.method == 'POST':
        nome = request.form['nome'].strip().lower()
        email = request.form['email'].strip().lower()

        if not nome or not email:
            return '<h2>Preencha todos os campos!</h2><a href="/registrar">Voltar</a>'

        resultado = blog.criar_usuario(nome, email)

        if resultado is not None:
            return f'<h2>Usuário {nome} criado com sucesso!</h2><a href="/">Voltar</a>'
        else:
            return f'<h2>Erro: este e-mail já está cadastrado.</h2><a href="/registrar">Tentar novamente</a>'

    return '''
        <h1>Registrar Novo Usuário</h1>
        <form method="post">
            Nome: <input type="text" name="nome"><br><br>
            Email: <input type="email" name="email"><br><br>
            <input type="submit" value="Registrar">
        </form>
        <a href="/">Voltar</a>
    '''
@app.route('/registrar_post', methods =['GET', 'POST'])
def criar_post():
    print("✅ Rota /registrar_post acessada")
    if request.method == 'POST':
        titulo = request.form['titulo'].strip().lower()
        conteudo = request.form['conteudo'].strip().lower()
        email_usuario = request.form['email_usuario'].strip().lower()

        if not all([titulo, conteudo, email_usuario]):
            return '<h2>Preencha todos os campos!</h2><a href="/registrar_post">Voltar</a>'

        usuario = blog.listar_usuarios_por_atributo("email", email_usuario)

        if usuario:
            resultado = blog.publicar_post(titulo, conteudo, email_usuario)
            if resultado:
                return f"<h2>Post criado com sucesso!</h2><a href='/post'>Ver posts</a>"
            else:
                return "<h2>Erro ao criar o post.</h2><a href='/registrar_post'>Tentar novamente</a>"
        else:
            return "<h2>Usuário não encontrado!</h2><a href='/registrar_post'>Tentar novamente</a>"
        
    return '''
        <h1>Criar Novo Post</h1>
        <form method="post">
            Título: <input type="text" name="titulo" required><br><br>
            Conteúdo: <textarea name="conteudo" rows="5" cols="30" required></textarea><br><br>
            Seu e-mail: <input type="email" name="email_usuario" required><br><br>
            <input type="submit" value="Publicar">
        </form>
        <a href="/">Voltar</a>
    '''


@app.route('/post', methods=['GET', 'POST'])
def listar_posts_na_web():
    print("✅ Rota /post acessada")

    if request.method == 'POST':
        atributo = request.form['atributo']
        valor = request.form['valor'].strip()
        posts = blog.listar_post_por_atributo(atributo, valor)
        print(f"🔍 Buscando por {atributo} = {valor}")
    else:
        posts = blog.listar_todos_os_post()

    if not posts:
        return '<h1>Ainda não há posts!</h1><a href="/post">Voltar</a>'

    html_da_pagina = "<h1>Todos os Posts</h1>"
    html_da_pagina += "<ul>"

    for post in posts:
        html_da_pagina += f"<li><a href='/post/{post.post_id}'>{post.titulo}</a> por <strong>{post.nome_autor}</strong></li>"

    html_da_pagina += "</ul>"
    html_da_pagina += '''
        <hr>
        <h3>Buscar post por atributo</h3>
        <form method="post">
            <label for="atributo">Buscar por:</label>
            <select name="atributo">
                <option value="titulo">Título</option>
                <option value="nome">Nome do autor</option>
                <option value="email">Email do autor</option>
            </select>
            <input type="text" name="valor" required>
            <input type="submit" value="Buscar">
        </form>
        <br>
        <a href="/">Voltar para página inicial</a>
    '''

    return html_da_pagina


@app.route('/post/<int:post_id>')
def detalhes_do_post(post_id):
    print("✅ Rota /post acessada")
    post = blog.listar_post_por_id(post_id)
    print("🔎 Conteúdo retornado:", post)
    if post:
        return f"""
            <h1>{post.titulo}</h1>
            <p>{post.conteudo}</p>
            <a href='/post'>Voltar</a>
        """ 
    else:
        return  "<h1>Post não encontrado</h1>", 404


if __name__ == '__main__':
    app.run(debug=True)