import csv
import json
import os





def get_urls_files(directory):
    urls = []
    name_files = []
    for root, dirs, files in os.walk(directory):
        if ".git" not in  root:
            for file in files:
                urls.append(os.path.join(root, file))
                name_files.append(file)
    return urls, name_files


class Read:
    def __init__(self, directory: str):
        """
        Read url file

        Args:
            directory (str): url file.
        """
        try:
            self.directory = directory
            self.urls, self.name_files = get_urls_files(directory)
            self.data_all = {}
            self.split_name_file(self.name_files,self.urls)
            # self.read_file(self.urls)
        except Exception as e:
            print(f'Error: {e}')

    def split_name_file(self, name_files: list, urls: list) -> None:
        for name_file in name_files:
            lis_name_file = name_file.split(".")
            print(lis_name_file[-1])
            if lis_name_file[-1] == "json":
                self.read_file_json(name_files,urls)
            elif lis_name_file[-1] == "csv":
                self.read_file_csv(name_files, urls)
            else:
                self.read_file(name_files, urls)

    def read_file_json(self, name_files: list, urls: list) -> None:
        try:
            for url_file in urls:
                with open(url_file, "r") as file:
                    content = json.load(file)
                    print("content")
                    break
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file_csv(self, name_files: list, urls: list) -> None:
        try:
            for url_file in urls:
                with open(url_file, "r") as file:
                    content = csv.DictReader(file)
                    print(content)
                    break
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)

    def read_file(self, name_files: list, urls: list) -> None:
        try:
            for url_file in urls:
                with open(url_file, "r") as file:
                    content = file.read()
                    # print(content)
                    break
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)