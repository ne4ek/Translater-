from check_english_GUI.check_english_GUI_json import CheckEnglishGUI
import tkinter as tk


def main():
    root = tk.Tk()
    app = CheckEnglishGUI(root, "words.json")
    root.mainloop()

if __name__ == "__main__":
    main()