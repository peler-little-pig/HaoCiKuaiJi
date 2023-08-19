import json


class Settings(staticmethod):
    with open('./AppData/setting/setting.json', 'r', encoding='utf-8') as j:
        settings = json.load(j)

    @staticmethod
    def save_data():
        with open("./AppData/setting/setting.json", "w", encoding='utf-8') as f:
            json.dump(Settings.settings, f)
