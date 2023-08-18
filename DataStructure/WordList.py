import csv
from typing import List

from DataStructure.Word import Word


class WordList(List):
    def __init__(self, group_name):
        super().__init__()
        self.group_name = group_name

    def load_word(self, path):
        csv_reader = list(csv.reader(open(path, encoding='utf-8')))
        for i in range(1, len(csv_reader)):
            self.append(Word(*csv_reader[i]))

    def remove(self, __value) -> None:
        for word in self:
            if word.word == __value:
                del word

    def save_word(self):
        with open(f'./AppData/dictionary/{self.group_name}/words.csv', 'w', encoding='utf-8', newline="") as f:
            csv_writer = csv.writer(f)
            header = ["word", "part_of_speech", "meaning", "example", "phonetic_symbol", "audio_link"]
            csv_writer.writerow(header)
            for word in self:
                csv_writer.writerow(word.get_value())

    def get_word(self, word_):
        for word in self:
            if word.word == word_:
                return word
        return None

    def __str__(self):
        result = ""
        for word in self:
            result += str(word) + "\n"
        return result
