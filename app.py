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

    for key, vuleo in data.data_all.items():
        # print(key)
        # print("++",vuleo)
        for index, item in enumerate(vuleo):
            cuont1 += 1
    print(cuont1)
    # print("--",data.urls)
    for key, vuleo in datac1.items():
        # print(key)
        # print("++",vuleo)
        for index, item in enumerate(vuleo):
            cuont2 += 1
    print(cuont2)