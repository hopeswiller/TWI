from flask import Flask
from . import controller


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.register_blueprint(controller.bp)

    return app
