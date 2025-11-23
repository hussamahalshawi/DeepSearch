import json
import os
import pandas as pd
import yaml
import xml.etree.ElementTree as ET
from docx import Document
from PyPDF2 import PdfReader
from PIL import Image
import wave



def get_urls_files(directory):
    # urls = []
    # name_files = []
    urls = {}
    for root, dirs, files in os.walk(directory):
        if ".git" not in  root:
            for file in files:
                urls[file] = os.path.join(root, file)
    return urls


class Read:
    def __init__(self, directory: str):
        """
        Read url file

        Args:
            directory (str): url file.
        """
        try:
            self.directory = directory
            self.urls = get_urls_files(directory)
            self.data_all = {}
            self.split_name_file(self.urls)
            # self.read_file(self.urls)
        except Exception as e:
            print(f'Error: {e}')

    def split_name_file(self, urls: dict) -> None:
        for name_file, url in urls.items():
            # print(name_file, url)
            self.data_all[name_file] = url
            lis_name_file = name_file.split(".")
            print(lis_name_file[-1])
            if lis_name_file[-1] == "txt":
                self.read_file_txt(name_file,url)
            elif lis_name_file[-1] == "json":
                self.read_file_json(name_file,url)
            elif lis_name_file[-1] == "csv":
                self.read_file_csv(name_file, url)
            elif lis_name_file[-1] == "yaml":
                self.read_file_yaml(name_file, url)
            elif lis_name_file[-1] == "xml":
                self.read_file_xml(name_file, url)
            elif lis_name_file[-1] == "xlsx" or lis_name_file[-1] == "xls":
                self.read_file_xlsx(name_file, url)
            elif lis_name_file[-1] == "docx":
                self.read_file_docx(name_file, url)
            elif lis_name_file[-1] == "pdf":
                self.read_file_pdf(name_file, url)
            elif lis_name_file[-1] == "png":###########
                self.read_file_image(name_file, url)
            elif lis_name_file[-1] == "mp3":###########
                self.read_file_audio(name_file, url)
            else:
                self.read_file(name_file, url)

    def read_file_txt(self, name_file, url) -> None:
        try:
            with open(url, "r") as file:
                content = file.read()
                # print(content)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file_json(self, name_file, url) -> None:
        try:
            with open(url, "r") as file:
                content = json.load(file)
                # print(content)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file_csv(self, name_file, url) -> None:
        try:
            df = pd.read_csv(url)
            # print(df)
            # with open(url, "r") as file:
            #     content = csv.DictReader(file)
            #     # print(content)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file_yaml(self, name_file, url) -> None:
        try:
            with open(url) as file:
                data = yaml.safe_load(file)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)

    def read_file_xml(self, name_file, url) -> None:
        try:
            tree = ET.parse(url)
            root = tree.getroot()
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)

    def read_file_xlsx(self, name_file, url) -> None:
        try:
            df = pd.read_excel(url)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file_docx(self, name_file, url) -> None:
        try:
            doc = Document(url)
            for p in doc.paragraphs:
                print(p.text)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)

    def read_file_pdf(self, name_file, url) -> None:
        try:
            reader = PdfReader(url)
            for page in reader.pages:
                print(page.extract_text())
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file_image(self, name_file, url) -> None:
        try:
            img = Image.open(url)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file_audio(self, name_file, url) -> None:
        try:
            with wave.open(url) as audio:
                print(audio.getparams())
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file(self, name_file, url) -> None:
        try:
            with open(url, "r") as file:
                content = file.read()
                # print(content)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)