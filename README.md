# translator
A simple app with Flask that can use as a translator
## Requirements
To run this app, you'll need to have Python 3 and the following Python packages installed:
 
1. Flask
2. googletrans

You can install these packages using pip by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository onto your local machine.
2. Install the required Python packages (see above).
3. Start the Flask app by running the following command in your terminal:
```bash
python run.py --host="http://127.0.0.1" --port=8000
```
4. The Flask app will start running on http://127.0.0.1:8000.
5. You can send a POST request to the /translate endpoint with a JSON payload containing the Persian text to be translated. For example:
```bash
curl -X POST -H 'Content-Type: application/json' -d '{"text": "سلام دنیا","source":"fa","target":"en"}' http://127.0.0.1:8000/translate
```
This will return a JSON object with the English translation of the input text.

## Supported Languages
<div align="center">

|          | Description                         | Supported |
|----------|-------------------------------------|-----------|
| en to fa | Translating english text to persian | &#9745;   |
| fa to en | Translating persian text to english | &#9745;   |
| fa to ar | Translating persian text to arabic  | &#9745;   |
| ar to fa | Translating arabic text to persian  | &#9745;   |
| ar to en | Translating arabic text to english  | &#9745;   |
| en to ar | Translating english text to arabic  | &#9745;   |

</div>