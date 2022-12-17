from flask import Flask

from app import __version__
from app.dynamic_modules import import_modules
from app.settings import MAPPINGS_PATH


def create_app() -> Flask:
    app = Flask(__name__)

    register_blueprints(app)

    @app.route("/healthz")
    def healthz() -> dict:
        return {"status": "healthy", "version": __version__}

    return app


def register_blueprints(app: Flask, path: str = MAPPINGS_PATH) -> None:
    for module in import_modules(path):
        app.register_blueprint(module.blueprint)
