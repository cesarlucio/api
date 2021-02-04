from flask import Flask
from alembic import op
import sqlalchemy as sa
import psycopg2

app = Flask(__name__)
con = psycopg2.connect(database="db_api_teste", user="root", password="root", host="localhost", port="5432")
cur = con.cursor()
@app.route('/')
def hello():

    cur.execute('''  CREATE TABLE IF NOT EXISTS usuario
           (id     SERIAL PRIMARY KEY ,
           name   TEXT NOT NULL,
           document TEXT UNIQUE,
           age     INT);
           ''')
    con.commit()

    return "Bem vindo"

@app.route("/cadastrar/<string:name>/<string:document>/<int:age>")
def cadastrar(name,document,age):
    cur = con.cursor()
    sql = "INSERT INTO usuario (name,document,age) values (%s, %s, %s)"
    try:
        cur.execute(sql,(name,document,age))

    except:
        resposta = "erro"
        con.rollback()

    else:
        resposta = "cadastrado"
        con.commit()

    return resposta


if __name__ == '__main__':
    app.run(debug=True, port=3000)

con.close()


