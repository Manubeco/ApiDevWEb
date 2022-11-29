from flask import Flask, jsonify, make_response, request
from bDados import Conta
from functions import alterar_conta,procura_conta

app = Flask(__name__)


@app.route('/cadastra/conta', methods=["POST"])
def add_user():
    new_user = request.json

    #
    # if "nome" not in newUser:
    #     return {"Status": 400, "mensagem": "O nome é obrigatório."}
    #
    # if "email" not in newUser:
    #     return {"Status": 400, "mensagem": "O email é obrigatório."}
    #
    # if "senha" not in newUser:
    #     return {"Status": 400, "mensagem": "A Senha é obrigatória."}
    # #
    # if len(senha) < 6:
    #     return GeraResposta("senha inválida", "Sua senha deve ter pelo menos 6 caracteres.")
    #
    # if "@" not in newUser:
    #     return GeraResposta("email inválido", "Verifique seu email e tente novamente.")

    Conta.append(new_user)

    return make_response(
        jsonify(mensagem="Conta cadastrada com sucesso!")
    )


@app.route('/exibir_conta', methods=["GET"])
def exibir_conta():
    id_conta = request.get_data()

    return make_response(
        jsonify(procura_conta(id_conta))
    )

@app.route('/editar_conta', methods=["PUT"])
def editar_conta():

    alterar_conta()

    return "deu certo"





app.run()
