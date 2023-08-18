import re
import os
import csv
import requests
from bs4 import BeautifulSoup


URL_CRAWL = "https://www.idealista.pt/arrendar-casas/lisboa/"


class CrawlerIdealista:
    def __init__(self):
        page = 1
        self.send_log_system('DEBUG', 'Start Crawler')

        while True:
            page = self.parse_place_list(page)
            if not page:
                break

        self.send_log_system('DEBUG', 'Finish Crawler')


    def parse_place_list(self, page):
        self.send_log_system('REQUEST', URL_CRAWL + f"pagina-{page}")

        place_request = requests.get(
            URL_CRAWL + f"pagina-{page}",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "accept-language": "pt-BR,pt;q=0.9",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            }
        )
        soup = BeautifulSoup(place_request.content, "html.parser")

        for place in soup.select("main#main-content article.item.extended-item.item-multimedia-container"):
            place_json = {
                "title": self.string_process(place, "div.item-info-container a.item-link"),
                "url": self.string_process(place, "div.item-info-container a.item-link", link=True),
                "price": self.string_process(place, "span.item-price.h2-simulated"),
                "typology": self.string_process(place, "div.item-detail-char span:nth-of-type(1)"),
                "area": self.string_process(place, "div.item-detail-char span:nth-of-type(2)"),
                "description": self.string_process(place, "div.item-description.description p")
            }
            self.send_log_system('DEBUG', place_json["url"])

            self.save_to_csv(place_json)

        if not soup.select_one("a.icon-arrow-right-after"):
            return None
        return page + 1

    def string_process(self, place, string, link=False):
        obj_soup = place.select_one(string)
        if obj_soup:
            if not link:
                string_ = str(obj_soup.text).replace("\n", "").strip()
                return re.sub(' +', ' ', string_)
            else:
                return "https://www.idealista.pt" + str(obj_soup["href"]).strip()
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
                    "typology",
                    "area",
                    "description"
                ])
        
        with open('imoveis.csv', 'a+', encoding='utf-8', newline="") as csv_file:
            csvWriter = csv.writer(csv_file, delimiter=';')
            csvWriter.writerow([
                place["title"],
                place["url"],
                place["price"],
                place["typology"],
                place["area"],
                place["description"]
            ])

CrawlerIdealista()