import json
import random

from DataStructure.WordList import WordList

STATUS_TEST = 0
STATUS_REVIEW_RECENT = 1
STATUS_REVIEW_ALL = 2


class SpellModel:
    def __init__(self, group):
        self.group = group
        self.dict = self.read_word_info()
        self.word_list = [d["word"] for d in self.dict]
        random.shuffle(self.word_list)
        self.word_list_split = self.chunk_list(self.word_list, 5)
        self.word_info = {item: 0 for item in self.word_list}
        print(self.word_info)

        self.review_recent_word_list = []
        self.review_all_word_list = []

        self.status = STATUS_TEST

    def chunk_list(self, lst, chunk_size):
        return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

    def wrong(self, word):
        self.word_info[word] += 1
        self.review_all_word_list.append(word)

    def right(self, word):
        if self.word_info[word] > 0:
            self.word_info[word] -= 1

    def read_word_info(self):
        word_list = WordList(self.group)
        word_list.load_word(f'./AppData/dictionary/{self.group}/words.csv')
        result = []
        for word in word_list:
            dict_ = {
                'word': word.word,
                'part_of_speech': word.part_of_speech,
                'chinese_definitions_list': word.meaning,
                'example': word.example,
                'phonetic_symbol': word.phonetic_symbol,
                'audio_link': word.audio_link
            }
            result.append(dict_)
        return result

    def get_tips(self, word):
        for i in self.dict:
            if i['word'] == word:
                return i['example'].split(";;")[0]

    def get_phonetic_symbol(self, word):
        for i in self.dict:
            if i['word'] == word:
                return i['phonetic_symbol']

    def get_next_word_test(self):
        if self.status == STATUS_TEST:
            # 清除空列表
            if not self.word_list_split[0]:
                del self.word_list_split[0]
                if self.word_list_split:
                    self.status = STATUS_REVIEW_RECENT
                    return self.get_next_word_review_recent()
                else:
                    self.status = STATUS_REVIEW_ALL
                    return self.get_next_word_review_all()
            else:
                item = self.word_list_split[0].pop()
                self.review_recent_word_list.append(item)
                print(self.word_list_split)
                return item

    def get_next_word_review_recent(self):
        if self.status == STATUS_REVIEW_RECENT:
            if self.review_recent_word_list:
                random.shuffle(self.review_recent_word_list)
                item = self.review_recent_word_list.pop()
                print(self.review_recent_word_list)
                return item
            else:
                self.status = STATUS_TEST
                return self.get_next_word_test()

    def get_next_word_review_all(self):
        if self.status == STATUS_REVIEW_ALL:
            if self.review_all_word_list:
                random.shuffle(self.review_all_word_list)
                item = self.review_all_word_list.pop()
                return item
            else:
                return None

    def get_next_word(self):
        if self.status == STATUS_TEST:
            return self.get_next_word_test()
        elif self.status == STATUS_REVIEW_RECENT:
            return self.get_next_word_review_recent()
        elif self.status == STATUS_REVIEW_ALL:
            return self.get_next_word_review_all()

    def get_chinese_definitions(self, word):
        for w in self.dict:

            if w['word'] == word:
                return random.choice(w['chinese_definitions_list'].split(";;")[:-1])
