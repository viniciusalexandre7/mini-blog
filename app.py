from flask import Flask
from logic import Blog
from models import Post, Usuario

app = Flask(__name__)

blog = Blog()

@app.route('/')
def pagina_inicial():
    return "<h1>Página Inicial do Blog</h1> <a href='/post'>Ver todos os posts</a>"

@app.route('/post')
def listar_posts_na_web():
    print("✅ Rota /post acessada")
    posts = blog.listar_todos_os_post()
    print("🔎 Conteúdo retornado:", posts)
    
    posts = blog.listar_todos_os_post()

    if not posts:
        return '<h1>Ainda não há posts!</h1>'

    html_da_pagina = "<h1>Todos os Posts</h1>"
    html_da_pagina += "<ul>"

    
    for post in posts:
        html_da_pagina += f"<li><a href='/post/{post.post_id}'>{post.titulo}</a> por {post.nome_autor}</li>"

    html_da_pagina += "</ul>"
    return html_da_pagina




if __name__ == '__main__':
    app.run(debug=True)