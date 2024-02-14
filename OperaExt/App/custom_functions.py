import json
import requests as req

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


def delete_word_from_json(file_name: str, word: str) -> None:
    with open(file_name, "r", encoding="utf-8") as file:
        file_in_python_format: dict = json.load(file)
        file_in_python_format.pop(word, None)
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(file_in_python_format, file, ensure_ascii=False, indent=1)

def get_last_word_from_json(file_name: str) -> str:
    with open(file_name, "r", encoding="utf-8") as file:
        file_in_python_format: dict = json.load(file)
        last_word = tuple(file_in_python_format.keys())[-1]
        print(last_word)
    return last_word