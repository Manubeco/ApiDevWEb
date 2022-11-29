from flask import Flask, jsonify, make_response, request
from bDados import Conta


# def add_user():
#     new_user = request.json
#
#     Conta.append(newUser)
#
#     return make_response(
#         jsonify(usuario=nome,
#                 mensagem="Conta cadastrada com sucesso!"
#                 )
#     )


def alterar_conta(account_id):
    nova_conta = {
        "id": 3,
        "Nome": "Fernando",
        "Email": "anagabip@gmail.com",
        "Senha": "quadrado3245"
    }

    for i in range(len(Conta)):
        for k, v in Conta[i].items():
            if v == account_id:
                Conta[i] = nova_conta


def procura_conta(id_conta):
    for i in range(len(Conta)):
        for k, v in Conta[i].items():
            if v == id_conta:
                print(Conta[id_conta])

# @app.route('/exibir_conta', methods=["GET"])
# def exibir_conta():
#     return make_response(
#         jsonify(Conta)
#     )
