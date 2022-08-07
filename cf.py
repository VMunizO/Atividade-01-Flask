from crypt import methods
from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import request



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html') 
    

@app.route("/cad/usuario")
def usuario():
    return render_template('user.html', titulo="Cadastro de Usuario")


@app.route("/cad/caduser", methods=['POST'])
def caduser():
    return request.form


@app.route("/cad/anuncio")
def anuncio():
    return render_template('anuncio.html', titulo="Anuncios")


@app.route("/anuncio/pergunta")
def pergunta():
    return render_template('pergunta.html', titulo="Perguntas")


@app.route("/anuncio/compra")
def compra():
    return render_template('compra.html', titulo="Compras")


@app.route("/anuncio/favoritos")
def favoritos():
    return render_template('favorito.html', titulo="Favoritos")

@app.route("/config/categoria")
def categoria():
    return render_template('categoria.html', titulo="Categorias")

@app.route("/relatorio/vendas")
def rel_vendas():
    return render_template('relvendas.html', titulo="Relatórios Vendas")

@app.route("/relatorio/compras")
def rel_compras():
    return render_template('relcompras.html', titulo="Relatórios Compras")


    