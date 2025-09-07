from myapp import app
from flask import render_template

@app.route("/")
def homepage(): 
    return render_template("sst.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/conteudos")
def conteudos():
    return render_template("btn_conteudos.html")

@app.route("/conteudos_1ANO")
def conteudos_1():
    return render_template("1_ano.html")

@app.route("/portugues_1Ano")
def portugues_1():
    return render_template("portugues_1ano.html")

@app.route("/ingles_1Ano")
def ingles_1():
    return render_template("ingles_1ano.html")

