from flask import Blueprint, jsonify

HELLO_MESSAGE = "<p>Hello, world!</p>"

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return jsonify(message=HELLO_MESSAGE)
