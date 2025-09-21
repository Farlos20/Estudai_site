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

@app.route("/Artes_2Ano")
def Artes_2():
    return render_template("2_Ano/artes_2ano.html")

@app.route("/Historia_2Ano")
def Historia_2():
    return render_template("2_Ano/historia_2ano.html")

@app.route("/Geografia_2Ano")
def Geografia_2():
    return render_template("2_Ano/geografia_2ano.html")

@app.route("/Biologia_2Ano")
def Biologia_2():
    return render_template("2_Ano/biologia_2ano.html")

@app.route("/Fisica_2Ano")
def Fisica_2():
    return render_template("2_Ano/fisica_2ano.html")

@app.route("/Quimica_2Ano")
def Quimica_2():
    return render_template("2_Ano/quimica_2ano.html")

@app.route("/Matematica_2Ano")
def Matematica_2():
    return render_template("2_Ano/matematica_2ano.html")

@app.route("/Sociologia_2Ano")
def Sociologia_2():
    return render_template("2_Ano/sociologia_2ano.html")

@app.route("/Filosofia_2Ano")
def Filosofia_2():
    return render_template("2_Ano/filosofia_2ano.html")

## 3 ANO

@app.route("/conteudos_3ANO")
def conteudos_3():
    return render_template("3_ano.html")

@app.route("/Portugues_3Ano")
def Portugues_3():
    return render_template("3_Ano/portugues_3ano.html")

@app.route("/Ingles_3Ano")
def Ingles_3():
    return render_template("3_Ano/ingles_3ano.html")

@app.route("/Educação_Fisica_3Ano")
def Ed_Fisica_3():
    return render_template("3_Ano/ed_fisica_3ano.html")

@app.route("/Artes_3Ano")
def Artes_3():
    return render_template("3_Ano/artes_3ano.html")

@app.route("/Matematica_3Ano")
def Matematica_3():
    return render_template("3_Ano/matematica_3ano.html")

@app.route("/Historia_3Ano")
def Historia_3():
    return render_template("3_Ano/historia_3ano.html")

@app.route("/Geografia_3Ano")
def Geografia_3():
    return render_template("3_Ano/geografia_3ano.html")

@app.route("/Biologia_3Ano")
def Biologia_3():
    return render_template("3_Ano/biologia_3ano.html")

@app.route("/Fisica_3Ano")
def Fisica_3():
    return render_template("3_Ano/fisica_3ano.html")

@app.route("/Quimica_3Ano")
def Quimica_3():
    return render_template("3_Ano/quimica_3ano.html")

@app.route("/Filosofia_3Ano")
def Filosofia_3():
    return render_template("3_Ano/filosofia_3ano.html")

@app.route("/Sociologia_3Ano")
def Sociologia_3():
    return render_template("3_Ano/sociologia_3ano.html")