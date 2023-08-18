class Word(object):
    def __init__(self, word: str, part_of_speech: str, meaning: str, example: str, phonetic_symbol: str,
                 audio_link: str):
        self.word = word
        self.part_of_speech = part_of_speech
        self.meaning = meaning
        self.example = example
        self.phonetic_symbol = phonetic_symbol
        self.audio_link = audio_link

    def get_value(self):
        return self.word, self.part_of_speech, self.meaning, self.example, self.phonetic_symbol, self.audio_link

    def __str__(self):
        return f"单词:{self.word} 词性:{self.part_of_speech} 释义:{self.meaning} 例句:{self.example} 音标:{self.phonetic_symbol} 音频链接:{self.audio_link}"
