import json
import os
import pandas as pd
import yaml
import xml.etree.ElementTree as ET
from docx import Document
from PyPDF2 import PdfReader
from PIL import Image
import wave
# import cv2
import zipfile
from bs4 import BeautifulSoup
import sqlite3

from pygments.lexer import words


# from pydub import AudioSegment



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
            self.data_all[url] = []
            lis_name_file = name_file.split(".")
            self.data_all[url].append(lis_name_file[0])
            print(lis_name_file[-1])
            if lis_name_file[-1] == "txt":
                self.read_file_txt(url)
            elif lis_name_file[-1] == "json":
                self.read_file_json(url)
            elif lis_name_file[-1] == "csv":
                self.read_file_csv(name_file, url)
            elif lis_name_file[-1] == "yaml":
                self.read_file_yaml(name_file, url)
            elif lis_name_file[-1] == "xml":
                self.read_file_xml(name_file, url)
            elif lis_name_file[-1] == "xlsx" or lis_name_file[-1] == "xls":
                self.read_file_xlsx(name_file, url)
            # elif lis_name_file[-1] == "docx":
            #     self.read_file_docx(name_file, url)
            # elif lis_name_file[-1] == "pdf":
            #     self.read_file_pdf(name_file, url)
            elif lis_name_file[-1] == "png":###########
                self.read_file_image(name_file, url)
            elif lis_name_file[-1] == "mp3":###########
                self.read_file_audio(name_file, url)
            # elif lis_name_file[-1] == "mp4":  ###########
            #     self.read_file_video(name_file, url)
            elif lis_name_file[-1] == "zip":  ###########
                self.read_file_zip(name_file, url)
            elif lis_name_file[-1] == "html":  ###########
                self.read_file_html(name_file, url)
            elif lis_name_file[-1] == "py":  ###########
                self.read_file_code(name_file, url)
            elif lis_name_file[-1] == "db":  ###########
                self.read_file_databace(name_file, url)
            else:
                self.read_file(name_file, url)

    def read_file_txt(self, url) -> None:
        try:
            with open(url, "r") as file:
                content = file.read()
            words = content.split()
            self.data_all[url].extend(words)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file_json(self, url) -> None:
        try:
            with open(url, "r") as file:
                content = json.load(file)
            self.extract_text_json_yaml(content, url)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)

    def extract_text_json_yaml(self, data, url):
        try:
            # print(data)
            if isinstance(data, dict):
                for key, value in data.items():
                    # print(key)
                    self.data_all[url].append(key)
                    self.extract_text_json_yaml(value, url)
            elif isinstance(data, list):
                for item in data:
                    self.extract_text_json_yaml(item, url)
            elif isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
                self.data_all[url].append(data)

        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file_csv(self, name_file, url) -> None:
        try:
            df = pd.read_csv(url)
            for col in df.columns:
                self.data_all[url].append(col)
                for value in df[col].astype(str):
                    for word in value.split():
                        self.data_all[url].append(word)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file_yaml(self, name_file, url) -> None:
        try:
            with open(url) as file:
                content = yaml.safe_load(file)
                self.extract_text_json_yaml(content, url)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file_xml(self, name_file, url) -> None:
        try:
            tree = ET.parse(url)
            root = tree.getroot()
            texts = [
                elem.text.strip()
                for elem in root.iter()
                if elem.text and elem.text.strip()
            ]
            words = []
            for item in texts:
                words.extend(item.split())
            self.data_all[url].extend(words)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)

    def read_file_xlsx(self, name_file, url) -> None:
        try:
            df = pd.read_excel(url)
            # df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            words = []
            for col in df.columns:
                print(col)
                if "Unnamed" not in str(col):    # تجاهل النصوص الفارغة
                    words.append(col)
                for value in df[col]:
                    if pd.notna(value):  # تجاهل القيم الفارغة
                        value = str(value).strip()  # تحويل لنص وتنظيفه
                        if value:  # تجاهل النصوص الفارغة
                            print(value)
                            words.extend(value.split())
            self.data_all[url].extend(words)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    # def read_file_docx(self, name_file, url) -> None:
    #     try:
    #         doc = Document(url)
    #         for p in doc.paragraphs:
    #             print(p.text)
    #     except FileNotFoundError:
    #         print("The file doesn't exist.")
    #     except Exception as e:
    #         print("An error occurred:", e)

    # def read_file_pdf(self, name_file, url) -> None:
    #     try:
    #         reader = PdfReader(url)
    #         for page in reader.pages:
    #             print(page.extract_text())
    #     except FileNotFoundError:
    #         print("The file doesn't exist.")
    #     except Exception as e:
    #         print("An error occurred:", e)


    def read_file_image(self, name_file, url) -> None:
        try:
            img = Image.open(url)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file_audio(self, name_file, url) -> None:
        try:
            pass
            # audio = AudioSegment.from_file("file.mp3")
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)

    # def read_file_video(self, name_file, url) -> None:
    #     try:
    #         video = cv2.VideoCapture(url)
    #
    #     except FileNotFoundError:
    #         print("The file doesn't exist.")
    #     except Exception as e:
    #         print("An error occurred:", e)

    def read_file_zip(self, name_file, url) -> None:
        try:
            with zipfile.ZipFile(url) as z:
                pass
                # df = z.extractall()
                # print(df)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)

    def read_file_html(self, name_file, url) -> None:
        try:
            with open(url) as file:
                soup = BeautifulSoup(file, "html.parser")
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)
    def read_file_code(self, name_file, url) -> None:
        try:
            with open(url) as file:
                content = file.read()
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)
    def read_file_databace(self, name_file, url) -> None:
        try:
            conn = sqlite3.connect(url)
            cursor = conn.cursor()
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)


    def read_file(self, name_file, url) -> None:
        try:
            pass
            # with open(url, "r") as file:
            #     content = file.read()
            #     # print(content)
        except FileNotFoundError:
            print("The file doesn't exist.")
        except Exception as e:
            print("An error occurred:", e)