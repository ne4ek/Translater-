import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime, timedelta

class CheckEnglishGUI:
    def __init__(self, root, file_path):
        self.root = root
        self.root.title("Flashcard App")
        self.root.geometry("400x300")
        
        self.container = ttk.Frame(root)
        self.container.pack(fill="both", expand=True)
        
        self.pages = {}
        
        with open(file_path, 'r', encoding='utf-8') as file:
            self.all_words = json.load(file)
            
        self.today = datetime.now()
        self.today_words = [
            word for word in self.all_words 
            if self.is_due_today(word['date'])
        ]
        self.current_card_index = 0
        
        self.create_pages()
        self.show_page("WordPage")
        
    def is_due_today(self, date):
        word_date = datetime(date['year'], date['month'], date['day'])
        return word_date.date() <= self.today.date()
        
    def create_pages(self):
        word_page = ttk.Frame(self.container)
        word_page.pack(fill="both", expand=True)
        
        self.eng_display = ttk.Label(
            word_page, 
            text="", 
            font=("Arial", 18)
        )
        self.eng_display.pack(pady=50)
        
        next_button = ttk.Button(
            word_page, 
            text="Next",
            command=lambda: self.show_page("AnswerPage")
        )
        next_button.pack(pady=20)
        
        self.pages["WordPage"] = word_page
        
        answer_page = ttk.Frame(self.container)
        answer_page.pack(fill="both", expand=True)
        
        self.eng_answer = ttk.Label(
            answer_page, 
            text="", 
            font=("Arial", 18)
        )
        self.eng_answer.pack(pady=20)
        
        self.ru_answer = ttk.Label(
            answer_page, 
            text="", 
            font=("Arial", 18)
        )
        self.ru_answer.pack(pady=20)
        
        button_frame = ttk.Frame(answer_page)
        button_frame.pack(pady=20)
        
        again_button = ttk.Button(
            button_frame, 
            text="Again",
            command=self.again_card
        )
        again_button.pack(side="left", padx=10)
        
        hard_button = ttk.Button(
            button_frame, 
            text="Hard",
            command=self.hard_card
        )
        hard_button.pack(side="left", padx=10)
        
        easy_button = ttk.Button(
            button_frame, 
            text="Easy",
            command=self.easy_card
        )
        easy_button.pack(side="left", padx=10)
        
        self.pages["AnswerPage"] = answer_page
    
    def show_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
        
        self.pages[page_name].pack(fill="both", expand=True)
        
        if self.current_card_index < len(self.today_words):
            current_word = self.today_words[self.current_card_index]
            if page_name == "WordPage":
                self.eng_display.config(text=current_word["eng_word"])
            else:
                self.eng_answer.config(text=current_word["eng_word"])
                self.ru_answer.config(text=current_word["ru_word"])
        else:
            self.eng_display.config(text="No more words for today!")
            self.eng_answer.config(text="No more words!")
            self.ru_answer.config(text="Come back tomorrow!")
    
    def save_words(self):
        with open('words.json', 'w', encoding='utf-8') as file:
            json.dump(self.all_words, file, ensure_ascii=False, indent=2)
    
    def update_word_date(self, days):
        if self.current_card_index < len(self.today_words):
            current_word = self.today_words[self.current_card_index]
            new_date = self.today + timedelta(days=days)
            
            for word in self.all_words:
                if word["eng_word"] == current_word["eng_word"]:
                    word["date"] = {
                        "day": new_date.day,
                        "month": new_date.month,
                        "year": new_date.year
                    }
            
            self.save_words()
            self.current_card_index += 1
            self.show_page("WordPage")
    
    def again_card(self):
        self.today_words.append(self.today_words[self.current_card_index])
        self.update_word_date(0)
    
    def hard_card(self):
        self.update_word_date(1)
    
    def easy_card(self):
        self.update_word_date(10)

