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
    return render_template("1_Ano/portugues_1ano.html")

@app.route("/ingles_1Ano")
def ingles_1():
    return render_template("1_Ano/ingles_1ano.html")

@app.route("/Educação_fisica_1Ano")
def ed_fisica_1():
    return render_template("1_Ano/ed_fisica_1ano.html")

@app.route("/Artes_1Ano")
def artes_1():
    return render_template("1_Ano/artes_1ano.html")

@app.route("/Matematica_1Ano")
def mat_1():
    return render_template("1_Ano/mat_1ano.html")

@app.route("/Fisica_1Ano")
def Fisica_1():
    return render_template("1_Ano/fisica_1ano.html")

@app.route("/Biologia_1Ano")
def Biologia_1():
    return render_template("1_Ano/biologia_1ano.html")

@app.route("/Quimica_1Ano")
def Quimica_1():
    return render_template("1_Ano/quimica_1ano.html")

@app.route("/Historia_1Ano")
def Historia_1():
    return render_template("1_Ano/historia_1ano.html")

@app.route("/Geografia_1Ano")
def Geografia_1():
    return render_template("1_Ano/geografia_1ano.html")

@app.route("/Sociologia_1Ano")
def Sociologia_1():
    return render_template("1_Ano/sociologia_1ano.html")

@app.route("/Filosofia_1Ano")
def Filosofia_1():
    return render_template("1_Ano/filosofia_1ano.html")
  #2 ANO
@app.route("/conteudos_2ANO")
def conteudos_2():
    return render_template("2_ano.html")

@app.route("/Portugues_2Ano")
def Portugues_2():
    return render_template("2_Ano/portugues_2ano.html")

@app.route("/Ingles_2Ano")
def ingles_2():
    return render_template("2_Ano/ingles_2ano.html")

@app.route("/Educação_Fisica_2Ano")
def Educação_Fisica_2():
    return render_template("2_Ano/ed_fisica_2ano.html")
