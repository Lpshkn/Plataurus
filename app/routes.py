from app import app
from flask import render_template, request, jsonify


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return jsonify({"firstCommon": [[1, 3]],
                        "secondCommon": [[2, 4]]})
    return render_template('index.html')
