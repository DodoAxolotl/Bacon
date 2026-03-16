import json
import flask
from flask_cors import CORS
from bacon_distance import calculate_bacon_distance

server = flask.Flask(__name__)
CORS(server)


@server.route("/calc/<actor>")
def get_bacon_distance(actor: str):
    try:
        return str(calculate_bacon_distance(db, actor))
    except ValueError as error:
        return flask.jsonify({"error": error.args[0]}), 404


if __name__ == "__main__":
    with open("db.json") as file:
        db = json.load(file)
    server.run(debug=True)
