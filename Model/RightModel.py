import json


class RightModel:
    def __init__(self, dict):
        self.dict = dict
        print(self.dict)

    def get_word_info(self, word):
        for d in self.dict:
            if d['word'] == word:
                return d['part_of_speech'], d['chinese_definitions_list'], d['example'], d['phonetic_symbol']

    def get_audio_link(self, word):
        for i in self.dict:
            if i['word'] == word:
                return i['audio_link']