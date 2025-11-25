import re


class CleanData:
    def __init__(self, data: dict):
        """
        Read url file

        Args:
            data (dict): url file.
        """
        self.data = data
        self.paragraph = {}
        self.data_all_new = {}

    def clean1(self):
        for key, value in self.data.items():
            self.paragraph[key] = ' '.join(map(str, value))
        return self.paragraph

    def clean2(self, pattern):
        for key, value in self.data.items():
            self.data_all_new[key] = []
            for word in value:
                if type(word) == int or type(word) == float:
                    value.remove(word)
                else:
                    word_new = re.findall(pattern, word)
                    self.data_all_new[key].append(word_new)
            self.paragraph[key] = ' '.join(map(str, value))
        return self.paragraph, self.data_all_new