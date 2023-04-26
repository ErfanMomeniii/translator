from flask import Flask, request, jsonify
from app.providers import findProvider

app = Flask(__name__)


@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    source = data['source']
    target = data['target']
    result = findProvider(source, target)(source, target, text)
    return jsonify({'translation': result})
