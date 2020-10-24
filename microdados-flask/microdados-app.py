from flask import Flask
from flask import render_template
from flask import request
import os 
from flask_sqlalchemy import SQLAlchemy

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
    if request.form:
        inscricao = request.form.get("insc")
        result = db.engine.execute(f'SELECT NU_INSCRICAO , NU_NOTA_CN , NU_NOTA_CH , NU_NOTA_LC , NU_NOTA_MT , TP_LINGUA , TP_STATUS_REDACAO, NU_NOTA_REDACAO, ano from microdados WHERE NU_INSCRICAO = \'{inscricao}\'')
        candidatos = []
        for row in result:
            candidatos.append(Candidato(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))


    return render_template("home.html", candidatos =  candidatos)
  
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
