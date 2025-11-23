from constants import directory, text_search, pattern
from readfile import Read

if __name__ == "__main__":
    data = Read(directory)
    # print("--",data.urls)
    print("++",data.data_all)