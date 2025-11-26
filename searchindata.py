import re


class SearchInData:
    def __init__(self, textsearch: str):
       self.text1, self.text2 = self.filtertext(textsearch)
       self.text3 = textsearch
       self. score_output_search = {}

    def filtertext(self, textsearch):
        text1 = textsearch.split(" ")
        text2 = "".join(text1)
        return text1, text2

    def search1(self, paragraph):
        for key, value in paragraph.items():
            self.score_output_search[key] = (0, "")
            for text in self.text1:
                if re.search(text, value):
                    self.score_output_search[key] = (self.score_output_search[key][0] + 1, value)
                if re.search(self.text2, value):
                    self.score_output_search[key] = (self.score_output_search[key][0] + 1, value)
                if re.search(self.text3, value):
                    self.score_output_search[key] = (self.score_output_search[key][0] + 1, value)

    def search2(self, paragraph):
        for key, value in paragraph.items():
            for text in self.text1:
                if re.search(text, value):
                    self.score_output_search[key] = (self.score_output_search[key][0] + 1, value)
                if re.search(self.text2, value):
                    self.score_output_search[key] = (self.score_output_search[key][0] + 1, value)
                if re.search(self.text3, value):
                    self.score_output_search[key] = (self.score_output_search[key][0] + 1, value)
        return self.score_output_search
    def search3(self, data_new):
        pass
