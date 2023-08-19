import requests
from bs4 import BeautifulSoup

from DataStructure.Word import Word
from Lib.DataTransform import DataTransform as d

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}


class WordSearcher(staticmethod):
    @staticmethod
    def search_all(word):
        base_url = 'https://dictionary.cambridge.org/dictionary/english-chinese-simplified/'
        # 发送GET请求
        response = requests.get(base_url + word, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # 获取中文释义
            target_class = ['trans', 'dtrans', 'dtrans-se', 'break-cj']
            # 查找所有<span>元素
            all_spans = soup.find_all("span")
            # 使用列表推导式筛选具有目标类名的<span>元素
            definitions = [span for span in all_spans if span.get("class") == target_class]
            chinese_definitions = [definition.get_text() for definition in definitions]
            # 获取例句
            examples = soup.select('.eg.deg')
            example_list_english = [example.get_text() for example in examples]
            t = ['trans', 'dtrans', 'dtrans-se', 'hdb', 'break-cj']
            # 查找所有<span>元素
            all_spans = soup.find_all("span")
            # 使用列表推导式筛选具有目标类名的<span>元素
            definitions = [span for span in all_spans if span.get("class") == t]
            example_list_chinese = [definition.get_text() for definition in definitions]
            example_list = [item for pair in zip(example_list_english, example_list_chinese) for item in pair]
            # 获取词性
            parts_of_speech = soup.select('.pos.dpos')
            parts_of_speech_list = [pos.get_text() for pos in parts_of_speech]
            # 获取音标
            phonetic_symbol = '/' + soup.select('.ipa.dipa.lpr-2.lpl-1')[0].get_text() + '/'
            # 获取音频文件链接
            audio_element = soup.find('source', {'type': 'audio/mpeg'})
            audio_link = audio_element['src'] if audio_element else None

            return Word(word, d.list_to_str(parts_of_speech_list), d.list_to_str(chinese_definitions),
                        d.list_to_str(example_list), phonetic_symbol,
                        'https://dictionary.cambridge.org' + audio_link)
        else:
            return None

    @staticmethod
    def search_audio_link(word):
        base_url = 'https://dictionary.cambridge.org/dictionary/english-chinese-simplified/'
        # 发送GET请求
        response = requests.get(base_url + word, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # 获取音频文件链接
            audio_element = soup.find('source', {'type': 'audio/mpeg'})
            audio_link = audio_element['src'] if audio_element else None
            return 'https://dictionary.cambridge.org' + audio_link