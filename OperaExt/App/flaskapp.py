import json
import os
from flask import Flask, request
from flask_cors import CORS
import requests as req
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__, static_url_path='')

cors = CORS(app)
json_file_for_update = os.getenv('PATH_TO_JSON_FILE_INCLUDE')

@app.route("/convert", methods=["POST"])
def main():
    data = request.get_json()
    print("Word geted, ", data)

    original_word: str = data['text'][0].strip().lower()
    translated_word: str = translate(original_word)

    update_json_file(json_file_for_update, (original_word, translated_word))

    return "Text converted and saved."


def translate(word: str) -> str:
    headers = {"User-Agent":
                   "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"
               }
    response = req.get(
        f'https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&dt=bd&dt=rm&hl=en&sl=en&tl=ru&q={word}',
        headers=headers)
    translated_word = json.loads(response.text)[0][0][0]
    return translated_word


def update_json_file(file_name: str, words: tuple) -> None:
    with open(file_name, "r", encoding="utf-8") as file:
        file_in_python_format: dict = json.load(file)
        file_in_python_format.update({words[0]: words[1]})
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(file_in_python_format, file, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
