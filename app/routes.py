import json
import os

from app import app
from flask import render_template, request, jsonify

from plataurus.match import get_clear_matches
from app.constants import FLASK_HOSTNAME, FLASK_PORT


HOSTNAME = os.getenv('FLASK_HOSTNAME', FLASK_HOSTNAME)
PORT = os.getenv('FLASK_PORT', FLASK_PORT)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = json.loads(request.data)
        first_matches, second_matches = get_clear_matches(data['firstText'], data['secondText'])
        return jsonify({"firstCommon": first_matches,
                        "secondCommon": second_matches})
    return render_template('index.html', host=HOSTNAME, port=PORT)
