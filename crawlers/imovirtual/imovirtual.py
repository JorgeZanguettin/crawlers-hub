import csv
import os
import re
import requests
from bs4 import BeautifulSoup


URL_CRAWL = "https://www.imovirtual.com/arrendar/apartamento/lisboa/?nrAdsPerPage=72"


class CrawlerImovirtual:
    def __init__(self):
        page = 1
        self.send_log_system('DEGUB', 'Start Crawler')

        while True:
            page = self.parse_place_list(page)
            if not page:
                break

        self.send_log_system('DEGUB', 'Finish Crawler')
    
    def parse_place_list(self, page):
        self.send_log_system('REQUEST', URL_CRAWL + f"&page={page}")

        place_request = requests.get(
            URL_CRAWL + f"&page={page}",
            headers={
                "accept": "application/json, text/javascript, */*; q=0.01",
                "accept-language": "pt-BR,pt;q=0.9",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
            }
        )
        soup = BeautifulSoup(place_request.content, "html.parser")

        for place in soup.select("div.col-md-content.section-listing__row-content article"):
            place_json = {
                "title": self.string_process(place, "div.offer-item-details h3 a span span.offer-item-title"),
                "url": self.string_process(place, "div.offer-item-details h3 a", link=True),
                "price": self.string_process(place, "ul.params li.offer-item-price"),
                "typology": self.string_process(place, "ul.params li.offer-item-rooms.hidden-xs"),
                "area": self.string_process(place, "ul.params li.hidden-xs.offer-item-area"),
                "description": self.string_process(place, "div.offer-item-details p.text-nowrap ")
            }
            self.send_log_system('DEGUB', place_json["url"])

            self.save_to_csv(place_json)

        if soup.select_one("li.pager-next a.disabled"):
            return None
        return page + 1

    def string_process(self, place, string, link=False):
        obj_soup = place.select_one(string)
        if obj_soup:
            if not link:
                string_ = str(obj_soup.text).replace("\n", "").strip()
                return re.sub(' +', ' ', string_)
            else:
                return str(obj_soup["href"]).strip()
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

CrawlerImovirtual()