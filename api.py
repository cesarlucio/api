from flask import Flask, request
from banco import Banco

app = Flask(__name__)

@app.route('/')
def ola():

    return "bem vindo"

@app.route("/pessoa", methods=['POST'])
def cadastrar():
    dados = request.json
    name = dados['name']
    document = dados['document']
    age = dados['age']
    banco = Banco()
    resposta = banco.cadastrar(dados)

    return resposta

@app.route("/pessoa/buscar", methods=['GET'])
def buscar():
    dado = request.json
    banco = Banco()
    if dado:
        id = dado['id']
        resposta = banco.buscar(id)
    else:
        resposta = banco.buscar("")


    return str(resposta)
if __name__ == '__main__':
    app.run(debug=True, port=3000)


