from flask import Flask, request
from banco import Banco

app = Flask(__name__)

@app.route('/')
def ola():

    return "bem vindo"

@app.route("/pessoa", methods=['GET','POST'])
def cadastrar():
    dados = request.json
    name = dados['name']
    document = dados['document']
    age = dados['age']

    resposta = Banco.cadastrar(dados)

    return resposta

@app.route("/pessoa/buscar", methods=['GET'])
def buscar():
    banco = Banco()
    resposta = banco.buscar()
    print(resposta)

if __name__ == '__main__':
    app.run(debug=True, port=3000)


