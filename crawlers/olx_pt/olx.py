import csv
import os
import re
import requests
from bs4 import BeautifulSoup


URL_CRAWL = "https://www.olx.pt/imoveis/apartamento-casa-a-venda/apartamentos-arrenda/"


class CrawlerOLX:
    def __init__(self):
        page = 1
        self.send_log_system('DEBUG', 'Start Crawler')

        while True:
            page = self.parse_place_list(page)
            if not page:
                break

        self.send_log_system('DEBUG', 'Finish Crawler')
    
    def parse_place_list(self, page):
        self.send_log_system('REQUEST', URL_CRAWL + f"?page={page}")

        place_request = requests.get(
            URL_CRAWL + f"?page={page}",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "accept-language": "pt-BR,pt;q=0.9",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            }
        )
        soup = BeautifulSoup(place_request.content, "html.parser")

        for place in soup.select("div.listing-grid-container.css-d4ctjd div.css-1sw7q4x"):
            place_json = {
                "title": self.string_process(place, "h6.css-16v5mdi.er34gjf0"),
                "url": self.string_process(place, "a.css-rc5s2u", link=True),
                "price": self.string_process(place, "p.css-10b0gli.er34gjf0").replace("Negociável", ""),
            }
            if place_json["url"]:
                self.send_log_system('DEBUG', place_json["url"])
                self.save_to_csv(place_json)

        if not soup.select_one("a[data-testid=pagination-forward]"):
            return None
        return page + 1

    def string_process(self, place, string, link=False):
        obj_soup = place.select_one(string)
        if obj_soup:
            if not link:
                string_ = str(obj_soup.text).replace("\n", "").strip()
                return re.sub(' +', ' ', string_)
            else:
                partial_url = str(obj_soup["href"]).strip()
                if "https://" not in partial_url:
                    return "https://www.olx.com" + partial_url
                return partial_url
        return ""
    

    def send_log_system(self, type_message, message):
        print (f'[ {type_message} ] {message}')

    def save_to_csv(self, place):
        if "imoveis.csv" not in os.listdir():
            with open('imoveis.csv', 'w', encoding='utf-8', newline="") as csv_file:
                csvWriter = csv.writer(csv_file, delimiter=';')
                csvWriter.writerow([
                    "title",
                    "url",
                    "price",
                ])
        
        with open('imoveis.csv', 'a+', encoding='utf-8', newline="") as csv_file:
            csvWriter = csv.writer(csv_file, delimiter=';')
            csvWriter.writerow([
                place["title"],
                place["url"],
                place["price"],
            ])

CrawlerOLX()