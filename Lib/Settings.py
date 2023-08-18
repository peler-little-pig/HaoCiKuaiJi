import json

from SharedData.SettingData import SettingData


class Settings(staticmethod):
    with open('./AppData/setting/setting.json', 'r', encoding='utf-8') as j:
        settings = json.load(j)
    @staticmethod
    def load_setting():
        SettingData.is_audio_need_download = Settings.settings['is_audio_need_download']

    @staticmethod
    def change_is_audio_need_download(value):
        Settings.settings['is_audio_need_download'] = value
        SettingData.is_audio_need_download = value

    @staticmethod
    def save_data():
        with open("./AppData/setting/setting.json", "w", encoding='utf-8') as f:
            json.dump(Settings.settings, f)
