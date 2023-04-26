from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)


@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    source = data['source']
    target = data['target']
    translator = Translator()
    result = translator.translate(text, src=source, dest=target)
    return jsonify({'translation': result.text})


if __name__ == '__main__':
    app.run(debug=True)
