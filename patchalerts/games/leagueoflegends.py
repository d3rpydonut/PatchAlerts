from util import loader
from wrappers.update import Update
from games.base_class import Game


class LeagueOfLegends(Game):
	def __init__(self):
		super().__init__('League of Legends', homepage='https://leagueoflegends.com/')

	def scan(self):
		soup = loader.soup("https://na.leagueoflegends.com/en/news/game-updates/patch")
		elems = soup.find_all(attrs={"class": 'views-row'})
		for elem in elems:
			link = elem.find('a')
			img = elem.find('img')
			dsc = elem.find(attrs={"class": 'field-type-text-long'})
			ttl = elem.find('h4')
			_url = 'https://na.leagueoflegends.com' + link["href"]
			_title = ttl.text
			_img = 'https://na.leagueoflegends.com' + img['src']
			_desc = dsc.text
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, image=_img, color="#e6ac00")


if __name__ == "__main__":
	lol = LeagueOfLegends()
	for u in lol.scan():
		print(u)
