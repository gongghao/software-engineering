from bs4 import BeautifulSoup
import requests
import pandas as pd

url_root = "https://zh.wikipedia.org"
url = url_root + "/wiki/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

class Spider:
    def __init__(self, url):
        self.url = url
        self.html = self.get_html()

    def get_html(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
        req = requests.get(self.url, headers=headers)
        return req.text

    def url_parser(self):
        soup = BeautifulSoup(self.html, "lxml")
        title = soup.find("th", class_="sidebar-title").text
        relation = "include"
        heads = soup.find_all("th", class_="sidebar-heading")
        data = []
        for head in heads:
            head = head.text.replace("\n", "")
            data.append([title, relation, head])
        df = pd.DataFrame(data)
        df.to_csv("./data/data.csv", index=False, encoding="utf-8", mode="a")

    def get_next_urls(self):
        soup = BeautifulSoup(self.html, "lxml")
        urls = soup.find_all("td", class_="sidebar-content")
        next_url = []
        for url in urls:
            name = url.find("a").text
            url = url.find("a").get("href")
            next_url.append([name, url_root + url])
        return next_url

test = Spider(url)
test.url_parser()