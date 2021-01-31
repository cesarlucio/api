
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
   return "Bem vindo"

if __name__ == '__main__':
    app.run(debug=True, port=3000)
