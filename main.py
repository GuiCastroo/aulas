from flask import Flask, request
from http import HTTPStatus
import json
from model import cadastro_lojista


app = Flask(__name__)


@app.route('/cadastra-lojista', methods=['POST'])
def home():
    data = request.get_json()
    result = cadastro_lojista.cadastro(name=data["name"], email=data["email"], cpf=data["cpf"])
    return json.dumps({"message": f"Cadastrado com sucesso, este E seu id {result['id']}"}), HTTPStatus.CREATED


@app.route('/get-lojista/<email>', methods=['GET'])
def get(email):
    result = cadastro_lojista.get_lojista(email)
    if isinstance(result, dict):
        method = HTTPStatus.OK
    else:
        method = HTTPStatus.NOT_FOUND
    return json.dumps({"message": result}), method


#todo construir rota para edição da loja


if __name__ == '__main__':
    app.run()
