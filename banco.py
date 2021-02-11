import psycopg2

from decouple import config

conexao_banco = psycopg2.connect(database=config('DATABASE'),
                                 user=config('USERNAME'),
                                 password=config('PASSWORD'),
                                 host=config('HOST'),
                                 port=config('PORT'))
cursor = conexao_banco.cursor()

class Banco():

    def criar_tabela(self):

        cursor.execute('''  CREATE TABLE IF NOT EXISTS pessoa
            (id     SERIAL PRIMARY KEY ,
            name   TEXT NOT NULL,
            document TEXT UNIQUE,
            age     INT);
            ''')
        conexao_banco.commit()

    def cadastrar(self,dados):

        name = dados['name']
        document = dados['document']
        age = dados['age']
        insert_sql_statement = "INSERT INTO pessoa (name,document,age) values (%s, %s, %s)"
        try:
            cursor.execute(insert_sql_statement, (name, document, age))
        except:
            resposta = "erro"
            conexao_banco.rollback()

        else:
            resposta = "cadastrado"
            conexao_banco.commit()

        return resposta

    def buscar(self,id):
        if not id:
            cursor.execute("SELECT * from pessoa")
            resultado = cursor.fetchall()
        else:
            select_sql_where = "SELECT * from pessoa where id = %s"
            cursor.execute(select_sql_where, (id,))
            resultado = cursor.fetchall()


        return resultado



