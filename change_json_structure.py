import tkinter as tk
import json
from datetime import datetime

def initialize_dates():
    with open('all_words.json', 'r', encoding='utf-8') as file:
        words = json.load(file)
    
    today = datetime.now()
    initialized_words = []
    
    for eng_word, ru_word in words.items():
        word_data = {
            "eng_word": eng_word.upper(),
            "ru_word": ru_word.upper(),
            "date": {
                "day": today.day,
                "month": today.month,
                "year": today.year
            }
        }
        initialized_words.append(word_data)
    
    with open('words.json', 'w', encoding='utf-8') as file:
        json.dump(initialized_words, file, ensure_ascii=False, indent=1)
    
    return 'words.json'


if __name__ == "__main__":
    initialize_dates()
