from bs4 import BeautifulSoup
from urllib.request import urlopen

class parser_:

	raw_html = ''
	html = ''
	rez = []

	def __init__(self, url, path):
		self.url = url
		self.path = path

	def get_html(self):
		req = urlopen(self.url)
		self.raw_html = req.read()
		self.html = BeautifulSoup(self.raw_html, 'html.parser')

	def parsing(self):
		get_news = self.html.find_all('div', class_="articles-cell")

		for i in get_news:
			title = i.find('div', 'article-title').get_text(strip=True)
			desc = i.find('div', 'article-desc').get_text(strip=True)
			href = i.a.get('href')
			self.rez.append({

				'title' : title,# i.find('div', 'article-title').get_text(strip=True)
				'desc' : desc,#i.find('div', 'article-desc').get_text(strip=True)
				'href' : href,#  i.a.get('href')
				
				})

	def save(self):
		with open(self.path, 'w', encoding='utf-8') as file:
			i = 1
			for item in self.rez:
				file.write(f'Статья №{i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: https://www.e-katalog.ru{item["href"]}\n\n ------------\n\n')
				i += 1		

	def run(self):
		self.get_html()
		self.parsing()
		self.save()
		print('Well done')