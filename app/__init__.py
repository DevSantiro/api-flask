from flask   import Flask
from .routes import register_routes


def create_app():
    app = Flask(__name__)

    # Faz o autoimport das rotas definidas
    register_routes(app)

    return app
