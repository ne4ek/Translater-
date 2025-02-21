import json
import requests as req
from datetime import datetime

def translate(word: str) -> str:
    headers = {"User-Agent":
                   "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"
               }
    response = req.get(
        f'https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&dt=bd&dt=rm&hl=en&sl=en&tl=ru&q={word}',
        headers=headers)
    translated_word = json.loads(response.text)[0][0][0]
    return translated_word


def update_json_file(file_name: str, words: tuple[str, str]) -> None:
    with open(file_name, "r", encoding="utf-8") as file:
        file_in_python_format: list = json.load(file)
        today = datetime.now()
        file_in_python_format.append({"eng_word": words[0].upper(), "ru_word": words[1].upper(), "date": {"day": today.day, "month": today.month, "year": today.year}})
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(file_in_python_format, file, ensure_ascii=False, indent=1)


def delete_word_from_json(file_name: str, eng_word: str) -> None:
    with open(file_name, "r", encoding="utf-8") as file:
        file_in_python_format: list = json.load(file)
        for index, word in enumerate(file_in_python_format):
            if word["eng_word"] == eng_word.upper():
                file_in_python_format.pop(index)
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(file_in_python_format, file, ensure_ascii=False, indent=1)

def get_last_word_from_json(file_name: str) -> str:
    with open(file_name, "r", encoding="utf-8") as file:
        file_in_python_format: list = json.load(file)
        last_word = file_in_python_format[-1]
        print(last_word)
    return last_word