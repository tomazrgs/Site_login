from tela_login.manipula.usuario import Usuario,Contas

from tela_login.back.utils import leitura_json

from flask import Flask, render_template, request
import os

contas = Contas()
app = Flask(__name__)



@app.route("/")
def login():
    return render_template("index.html")

@app.route("/login")
def index():
    dados = leitura_json('dados.json')

    for dado in dados:
        dado = Usuario.from_dict(dado)
        contas.adduser(dado)   

    user = request.form('user')
    password = request.form('passwaord')

    valida = contas.verifica_login(user, password)


    if valida:
        return 'logado.html'

    pass

if __name__ == '__main__':
    app.run(debug=True, port = 5001)