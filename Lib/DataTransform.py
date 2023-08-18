class DataTransform(staticmethod):
    @staticmethod
    def list_to_str(l):
        result = ''
        for i in l:
            result += str(i) + ';;'
        return result
