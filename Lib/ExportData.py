import csv

from SharedData.DictionaryData import DictionaryData


class ExportData(staticmethod):
    @staticmethod
    def export_pure_table_csv(path):
        with open(path, 'w', encoding='Shift-JIS', newline="") as f:
            csv_writer = csv.writer(f)
            header = ["单词", "词性", "释义", "例子", "音标"]
            csv_writer.writerow(header)
            for word in DictionaryData.current_word_list:
                csv_writer.writerow(word.get_value()[:-1])