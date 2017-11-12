from flask import Flask, request, jsonify
from rend import parse
app = Flask(__name__)


@app.route("/")
def index_route():
    return "rend 1.0: parsing microservice"


@app.route("/parse", methods=['POST'])
def parse_route():
    body = request.get_json(force=True)
    try:
        data = parse.parse(body['programText'])

        return jsonify({'program': data}), 200
    except:
        return jsonify({'error': 'An error happened'}), 400
