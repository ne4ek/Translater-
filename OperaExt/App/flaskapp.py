import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from custom_functions import *

app = Flask(__name__, static_url_path='')

cors = CORS(app)
json_file_for_update: str = os.getcwd() + "/words.json"


@app.route("/sendWordForAdd", methods=["POST"])
def send_word_for_add():
    data = request.get_json()
    print("Word geted, ", data)

    original_word: str = data['text'][0].strip().lower()
    translated_word: str = translate(original_word).lower()

    update_json_file(json_file_for_update, (original_word, translated_word))
    return "Text converted and saved."


@app.route("/translateWord", methods=["GET"])
def translate_word():
    data = request.args.get("word")

    original_word: str = data.strip().lower()
    translated_word = translate(original_word)

    print("translate word - ", original_word, translated_word)
    response = jsonify({"translatedWord": translated_word})
    return response


@app.route('/deleteWord', methods=["DELETE"])
def delete_word():
    data = request.get_json()
    print("Word deleted, ", data)
    original_word: str = data['text'][0].strip().lower()

    delete_word_from_json(json_file_for_update, original_word)
    return "Delete successful"


@app.route('/deleteLastWord', methods=["DELETE"])
def delete_last_word():
    last_word_stuct = get_last_word_from_json(json_file_for_update)
    last_word = last_word_stuct["eng_word"]
    delete_word_from_json(json_file_for_update, last_word)
    print("Last word deleted, ", last_word)
    return "Delete successful last"


@app.route("/testPath", methods=["POST"])
def test_path():
    data = request.get_json()
    print('test', data)
    return "test successful"


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
