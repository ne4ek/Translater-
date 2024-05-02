import json
import os
from random import randint
from colorama import Fore






file_name = "/all_words.json"
file_path = os.getcwd() + file_name


class Eng:
    file: dict = json.load(open(file_path, encoding="utf-8"))
    right, wrong = 0, 0

    def _print(self) -> None:
        print(
            f'{Fore.CYAN}There were {self.right + self.wrong} attempts in total, right {self.right}, wrong {self.wrong}, in procent right {100 - round((self.wrong * 100 / (self.right + self.wrong)), 2)}%{Fore.RESET}')

    def run(self,
            start=0,
            end="all") -> None:
        if end == "all":
            end = len(self.file)

        words = {i: self.file[i] for i in list(self.file.keys())[start: end]}

        while words:
            words_keys = list(words.keys())

            rand = randint(0, len(words) - 1)
            inp = input(f"{Fore.RESET}{words[words_keys[rand]]}\t").lower()

            if inp == "stop":

                break
            elif inp == words_keys[rand]:
                print(f"{Fore.GREEN}{words_keys[rand]} \t {len(words) - 1}")
                del words[inp]
                self.right += 1
            else:
                print(f"{Fore.RED}{words_keys[rand]} \t {len(words)}")
                self.wrong += 1
        self._print()
        self.right, self.wrong = 0, 0


if __name__ == '__main__':
    f = Eng()
    f.run()
