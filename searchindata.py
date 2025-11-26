

class SearchInData:
    def __init__(self, textsearch: str):
       self.text1, self.text2 = self.filtertext(textsearch)
       self.text3 = textsearch

    def filtertext(self, textsearch):
        text1 = textsearch.split(" ")
        text2 = "".join(text1)
        return text1, text2

    def search1(self, paragraph):
        pass
    def search2(self, paragraph):
        pass
    def search3(self, data_new):
        pass
