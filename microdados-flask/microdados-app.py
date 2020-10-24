from flask import Flask
from flask import render_template
from flask import request
import os 
from flask_sqlalchemy import SQLAlchemy
from flask import session
from waitress import serve


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:rootdb@localhost/enem"

db = SQLAlchemy(app)

class Candidato():
    def __init__(self, insc, nota_cn, nota_ch, nota_lc, nota_mt, tp_lingua, tp_status_red, nota_redacao, ano):
        self.inscricao = insc
        self.nota_cn = nota_cn
        self.nota_ch = nota_ch
        self.nota_lc = nota_lc
        self.nota_mt = nota_mt
        self.tp_lingua =  tp_lingua
        self.tp_status_red = tp_status_red
        self.nota_redacao = nota_redacao
        self.ano = ano



@app.route("/", methods = ["GET", "POST"])
def home():
    candidatos = []
    invalidos = []
    if request.form:
        consulta = request.form.get("insc")
        valores = [ value.strip() for value in consulta.split(",") ]

        inscricoes = []
        for valor in valores:
            if valor.isnumeric():
                inscricoes.append(valor)
            else:
                invalidos.append(valor)

        if inscricoes:
            query = "SELECT NU_INSCRICAO , NU_NOTA_CN , NU_NOTA_CH , NU_NOTA_LC , NU_NOTA_MT , TP_LINGUA , TP_STATUS_REDACAO, NU_NOTA_REDACAO, ano from microdados WHERE NU_INSCRICAO IN ({})".format(",".join(["%s"]*len(inscricoes)))
            print (inscricoes)
            print (query)
            result = db.engine.execute(query, inscricoes)
            for row in result:
                candidatos.append(Candidato(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    session.clear()
    return render_template("home.html", candidatos =  candidatos, invalidos = invalidos)
  
if __name__ == "__main__":
    app.secret_key = b'_5#y2L"F4Q8zdasdq321243129'
    serve(app, host='0.0.0.0', port=80)

