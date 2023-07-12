from flask import Flask
import os


def register_router(flask_app: Flask):
    from .controller import todo_controller

    flask_app.register_blueprint(todo_controller.bp)


def set_exception_handler(flask_app: Flask):
    from .common.exception_handler import error_handle

    error_handle(flask_app)


def create_app():
    app = Flask(__name__)
    register_router(app)
    set_exception_handler(app)

    return app
