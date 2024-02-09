import os
from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
from functions import *

load_dotenv()

app = Flask(__name__, static_url_path='')

cors = CORS(app)
json_file_for_update = os.getenv('PATH_TO_JSON_FILE_INCLUDE')


@app.route("/sendWordForAdd", methods=["POST"])
def send_word_for_add():
    data = request.get_json()
    print("Word geted, ", data)

    original_word: str = data['text'][0].strip().lower()
    translated_word: str = translate(original_word)

    update_json_file(json_file_for_update, (original_word, translated_word))
    return "Text converted and saved."


@app.route("/testPath", methods=["POST"])
def test_path():
    data = request.get_json()
    print('test', data)
    return "test successful"

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
