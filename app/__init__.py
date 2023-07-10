from flask import Flask
import os


def register_router(flask_app: Flask):
    from .router import todo_router

    flask_app.register_blueprint(todo_router.bp)


def create_app():
    app = Flask(__name__)
    register_router(app)

    return app
