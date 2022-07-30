from flask import Flask, request
from http import HTTPStatus
import json
from lojista.controller.blue_cadastro import blue_lojista


def create_app():
    app = Flask(__name__)
    # Configure app
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////tmp/lojista.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # BluePrints registers
    app.register_blueprint(blue_lojista)

    @app.route('/', methods=['POST', 'GET'])
    def home():
        return json.dumps({"message": f"Bem-vindo!!"}), HTTPStatus.OK
    return app


if __name__ == '__main__':
    create_app().run()
