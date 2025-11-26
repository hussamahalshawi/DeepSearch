from cleandata import CleanData
from constants import directory, text_search, pattern
from readfile import Read

if __name__ == "__main__":
    cuont1 = 0
    cuont2 = 0
    data = Read(directory)
    datac = CleanData(data.data_all)
    datac1 = datac.clean1()
    datac2, data_new = datac.clean2(pattern)

    for key, value in data.data_all.items():
        # print(key)
        # print("++",value)
        for index, item in enumerate(value):
            cuont1 += 1
    print(cuont1)
    # print("--",data.urls)
    for key, value in data_new.items():
        # print(key)
        # print("++",value)
        for index, item in enumerate(value):
            cuont2 += 1
    print(cuont2)