from flask import Flask


app = Flask(__name__)

from viwer import *

if __name__ == "__main__":
    app.run(host='0.0.0.0')

#templates/ → todos os HTML

#static/ → CSS, JS, imagens

#viwer.py → define as rotas com @app.route(...)

#git add .
#git commit -m "Descrição da alteração"
#git push