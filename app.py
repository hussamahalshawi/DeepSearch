from constants import directory, text_search, pattern
from readfile import Read

if __name__ == "__main__":
    cuont = 0
    data = Read(directory)
    # print("--",data.urls)
    for key, vuleo in data.data_all.items():
        # print(key)
        # print("++",vuleo)
        for index, item in enumerate(vuleo):
            cuont += 1
    print(cuont)