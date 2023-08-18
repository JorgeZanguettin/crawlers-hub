import os
import sys
from datetime import datetime
from bs4 import BeautifulSoup
import cfscrape 
 

class CrawlerInvesting:
	def __init__(self):
		self.scraper = cfscrape.create_scraper()

		nomeCriptoMoeda = str(sys.argv[-1])
		if '.py' in nomeCriptoMoeda:
			self.sendLogToSystem('ERROR', 'Syntax de execução incorreta. Correta : python investing.py "Nome Criptomoeda"')
			quit()

		self.sendLogToSystem('DEBUG', 'Start Crawler')
		self.getCritoMoeda(nomeCriptoMoeda)
		self.sendLogToSystem('DEBUG', 'Finish Crawler')

	def sendLogToSystem(self, type_message, message):
		print (f'[ {type_message} ] {message}')

	def getCritoMoeda(self, nomeCriptoMoeda):
		nomeCriptoMoedaURL = nomeCriptoMoeda.replace(' ','-')

		urlCriptoMoeda = 'https://br.investing.com/crypto/{}'.format(nomeCriptoMoedaURL)

		requisicaoCriptoMoeda = self.scraper.get(urlCriptoMoeda) 

		if requisicaoCriptoMoeda.status_code == 200:
			soupCriptoMoeda = BeautifulSoup(requisicaoCriptoMoeda.text, 'html.parser')

			valorCriptoDolar = self.tratarStringToDouble(soupCriptoMoeda.select_one("span#last_last"))
			valorCriptoReal = valorCriptoDolar * self.getValueDolar()

			dictCriptoMoeda = {
				'nome_criptomoeda' : nomeCriptoMoeda,
				'url_criptoMoeda' : urlCriptoMoeda,
				'valor_dolar' : valorCriptoDolar,
				'valor_real' : valorCriptoReal,
				'valor_variacao' : self.tratarStringToDouble( soupCriptoMoeda.select_one('div.top.bold.inlineblock span:nth-of-type(2)') ),
				'porcentagem_variacao' : str(self.tratarStringToDouble( soupCriptoMoeda.select_one('div.top.bold.inlineblock span:nth-of-type(4)') ) )+'%',
				'data_hora_consulta' : datetime.now().strftime('%Y-%m-%d %H:%M:%S%z')
			}

			self.sendLogToSystem('DEBUG', 'Cotacão Coletada - {} | {}'.format(nomeCriptoMoeda,dictCriptoMoeda['data_hora_consulta']))

			self.setInfoInCSV(dictCriptoMoeda)
		else:
			self.sendLogToSystem('ERROR', 'Criptomoeda invalida')

	def tratarStringToDouble(self, string):
		if string != None:
			return float( str(string.text).replace('.','').replace(',','.').replace('%','').strip() )
		else:
			return None

	def setInfoInCSV(self, dictData):
		titles, data = self.convertDictInCSV(dictData)

		if 'cotacoes.csv' in os.listdir('./'):
			fileCSV = open('cotacoes.csv', 'a+', encoding='utf-8')
			fileCSV.write(data)
		else:
			fileCSV = open('cotacoes.csv', 'a+', encoding='utf-8')
			fileCSV.write(titles + data)

		fileCSV.close()

	def convertDictInCSV(self, dictData):
		arrayTitles = []
		arrayData = []

		for key in dictData:
			arrayTitles.append(str(key))
			arrayData.append(str(dictData[key]))

		stringTitle = str(';'.join(arrayTitles)) + '\n'
		stringData = str(';'.join(arrayData)) + '\n'

		return stringTitle, stringData

	def getValueDolar(self):
		urlDolar = 'https://br.investing.com/currencies/usd-brl'

		requisicaoDolar = self.scraper.get(urlDolar)
		soupDolar = BeautifulSoup(requisicaoDolar.text, 'html.parser')

		return self.tratarStringToDouble(soupDolar.select_one("span.text-2xl"))


CrawlerInvesting()
