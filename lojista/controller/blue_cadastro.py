from flask import Blueprint, jsonify, request
from http import HTTPStatus
import json
from model import cadastro_lojista


blue_lojista = Blueprint('lojista', __name__, url_prefix='/lojista')


@blue_lojista.route('/cadastro', methods=['POST'])
def home():
    data = request.get_json()
    result = cadastro_lojista.cadastro(name=data["name"], email=data["email"], cpf=data["cpf"])
    return json.dumps({"message": f"Cadastrado com sucesso, este E seu id {result['id']}"}), HTTPStatus.CREATED


@blue_lojista.route('/<email>', methods=['GET'])
def get(email):
    result = cadastro_lojista.get_lojista(email)
    if isinstance(result, dict):
        method = HTTPStatus.OK
    else:
        method = HTTPStatus.NOT_FOUND
    return json.dumps({"message": result}), method


#todo construir rota para edição da loja


def configure(app):
    pass