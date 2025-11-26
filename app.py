from cleandata import CleanData
from constants import directory, text_search, pattern
from readfile import Read
from searchindata import SearchInData

if __name__ == "__main__":
    cuont1 = 0
    cuont2 = 0
    data = Read(directory)
    cleandata = CleanData(data.data_all)
    paragraph1 = cleandata.clean1()
    paragraph2, data_new = cleandata.clean2(pattern)

    for key, value in data.data_all.items():
        # print(key)
        # print("++",value)
        for index, item in enumerate(value):
            cuont1 += 1
    print(cuont1)
    searchindata = SearchInData(text_search)
    output1 = searchindata.search1(paragraph1)
    for key, value in data_new.items():
        # print(key)
        # print("++",value)
        for index, item in enumerate(value):
            cuont2 += 1
    print(cuont2)