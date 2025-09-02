from myapp import app
from flask import render_template

@app.route("/")
def homepage(): 
    return render_template("sst.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")