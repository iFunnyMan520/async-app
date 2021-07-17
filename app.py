from flask import Flask


def make_app() -> Flask:
    from views.router import install

    app = Flask(__name__)

    install(app)

    return app
