from flask import Flask
from . import controller

def create_app(test_config = None):
    # create and configure the app
    app = Flask(__name__)

    app.register_blueprint(controller.bp)
    return app