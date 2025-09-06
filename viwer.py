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

@app.route("/conteudos_1")
def conteudos_1():
    return render_template("1_ano.html")
