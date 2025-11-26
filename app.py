from cleandata import CleanData
from constants import directory, text_search, pattern
from readfile import Read
from searchindata import SearchInData

if __name__ == "__main__":
    cuont1 = 0
    cuont2 = 0
    cuont3 = 0
    data = Read(directory)
    cleandata = CleanData(data.data_all)
    paragraph1 = cleandata.clean1()
    paragraph2, data_new = cleandata.clean2(pattern)


    for key, value in data.data_all.items():
        for index, item in enumerate(value):
            cuont1 += 1
    searchindata = SearchInData(text_search)
    searchindata.search1(paragraph1)
    searchindata.search2(paragraph2)
    searchindata.search3(data_new)
    output_search = searchindata.score_output_search
    sorted_by_output_search = dict(sorted(((key, value) for key, value in output_search.items() if value[0] != 0), key=lambda x: x[1][0], reverse=True))
    for key, value in sorted_by_output_search.items():
        print(value, key)
    for key, value in data_new.items():
        for index, item in enumerate(value):
            cuont3 += 1