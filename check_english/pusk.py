#This file for tests and run check_English_json file


from check_English_json import Eng

f = Eng()


state = 'a'

while state != 'exit':
    start = int(input(f"enter start point (all words - {f.file_len}) "))
    end = input(f"enter end point (all words - {f.file_len}) ")

    if end and end.isdigit:
        end = int(end)
    else:
        end = "all"
    f.run(start=start, end=end)
    state = input("type 'exit' for close or click anybutton for repeat")