from flask import Blueprint

blueprint = Blueprint("hello", __name__)


@blueprint.route("/hello")
def hello():
    return {"Hello": "World"}
