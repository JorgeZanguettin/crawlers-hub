import requests
import json
import csv
import os
from bs4 import BeautifulSoup


class CrawlerSteam:
    def __init__(self):
        start = 0
        end = 100
        
        self.get_all_games(
            f'https://store.steampowered.com/search/results/?query&start={start}&count={end}&dynamic_data=&sort_by=_ASC&specials=1&filter=topsellers&infinite=1'
        )

    def get_all_games(self, url):
        request_games = requests.get(url)
        obj_json = json.loads(request_games.content.decode('utf-8'))
        obj_bs4 = BeautifulSoup(obj_json['results_html'], "html.parser")
        
        for game_block in obj_bs4.select('a.search_result_row'):
            obj_game = BeautifulSoup(str(game_block), 'html.parser')
            
            self.save_to_csv({
                'name': self.tratar_strings(obj_game.select_one('div.col.search_name.ellipsis'), 'STR'),
                'url': self.tratar_strings(obj_game.select_one('a'), 'URL'),
                'release_date': self.tratar_strings(obj_game.select_one('div.col.search_released.responsive_secondrow'), 'STR'),
                'review_summary': self.tratar_strings(obj_game.select_one('span.search_review_summary'), 'STR_AVAL'),
                'start_price': self.tratar_strings(obj_game.select_one('div.discount_original_price'), 'STR'),
                'discount_pct': self.tratar_strings(obj_game.select_one('div.discount_pct'), 'STR'),
                'final_price': self.tratar_strings(obj_game.select_one('div.discount_final_price'), 'STR')
            })

    def tratar_strings(self, string, type_string):
        if type_string == 'STR':
            if string != None:
                return str(string.text).replace('\n','').replace('\t','').replace('\r','').replace(';','').strip()
            else:
                return ''
        elif type_string == 'URL':
            url = str(string['href']).strip()
            if "?" in url:
                url = url.split("?")[0].strip()
            return url
        elif type_string == 'STR_AVAL':
            if string != None:
                return str(string['data-tooltip-html']).replace('<br>','.').strip()
            else:
                return ''

    def save_to_csv(self, json_game):
        if "games.csv" not in os.listdir():
            with open('games.csv', 'w', encoding='utf-8', newline="") as csv_file:
                csvWriter = csv.writer(csv_file, delimiter=';')
                csvWriter.writerow([
                    'name',
                    'url',
                    'release_date',
                    'review_summary',
                    'start_price',
                    'discount_pct',
                    'final_price'
                ])
        
        print ('[ DEBUG ]', json_game['url'])
        with open('games.csv', 'a+', encoding='utf-8', newline="") as csv_file:
            csvWriter = csv.writer(csv_file, delimiter=';')
            csvWriter.writerow([
                json_game['name'],
                json_game['url'],
                json_game['release_date'],
                json_game['review_summary'],
                json_game['start_price'],
                json_game['discount_pct'],
                json_game['final_price']
            ])

CrawlerSteam()