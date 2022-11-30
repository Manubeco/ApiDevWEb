from flask import Flask, jsonify, make_response, request
from bDados import Conta

app = Flask(__name__)



@app.route('/conta', methods=["GET"])
def exibir_conta():

    return make_response(jsonify(Conta))


@app.route('/conta', methods=["POST"])
def add_user():
    new_user = request.json
    Conta.append(new_user)

    return make_response(
        jsonify(mensagem="Conta cadastrada com sucesso!"))


@app.route('/conta', methods=["PUT"])
def alterar_conta():
    nova_conta = request.get_json()
    
    for i in range(len(Conta)):
        for v in Conta[i].values():
            if v == 2:
                Conta[i] = nova_conta
                return "Conta alterada com sucesso!"

    
@app.route('/conta', methods=["DELETE"])
def apagar_conta():
     for i in range(len(Conta)):
        for v in Conta[i].values():
            if v == 1:
                Conta.pop(i)
                return make_response(jsonify(mensagem = "Conta apagada com sucesso!"))     

   
app.run()
