import json
import requests
from libs import DataPreview
from bs4 import BeautifulSoup
import os
import re


class Scraping:

    def __init__(self, url):
        self.url = url
        self.__GetDate()

    def __GetDate(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.content)
        self.sticker_name = soup.find(class_='mdCMN38Item01Ttl').text
        self.sticker_author = soup.find(class_='mdCMN38Item01Author').text
        self.sticker_description = soup.find(class_='mdCMN38Item01Txt').text
        self.sticker_price = soup.find(class_='mdCMN38Item01Price').text
        self.sticker_data = []

        for sticker in soup.find_all(True, {'class': ['mdCMN09Li', 'FnStickerPreviewItem']}):
            result = DataPreview.data_preview_from_dict(json.loads(sticker.get("data-preview")))
            self.sticker_data.append(result)


class SaveFile:
    def __init__(self, data, path_child, id):
        self.data = data
        self.path_child = path_child
        self.id = id
        self.check_path_result()

    def check_path_result(self):
        if os.path.exists("result"):
            self.check_path_child()
        else:
            os.mkdir("result")
            self.check_path_child()

    def check_path_child(self):

        if (os.path.exists(f"result/{self.path_child}")):
            self.saveFile()
        else:
            os.mkdir(f"result/{self.path_child}")
            self.saveFile()

    def saveFile(self):
        fs = open(f"result/{self.path_child}/{self.id}.png", "wb")
        fs.write(self.data)
        print(f"[SUCCESS] {self.path_child}/{self.id}.png")
        fs.close()
        return


if __name__ == '__main__':
    url = input("sticker line url : ")
    path_child = re.findall(r"\d*[0-9]",url)[0]

    scraping = Scraping(url=url)
    for item in scraping.sticker_data:
        res = requests.get(item.fallback_static_url)
        SaveFile(res.content,f"{path_child}_{scraping.sticker_author.replace(' ','-') }",f"{path_child}_{item.id}_{scraping.sticker_author.replace(' ','-')}")
