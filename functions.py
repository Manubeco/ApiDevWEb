from flask import Flask, jsonify, make_response, request
from bDados import Conta


def apagar():
    for i in range(len(Conta)):
        for v in Conta[i].values():
            if v == 1:
                Conta.pop[i]