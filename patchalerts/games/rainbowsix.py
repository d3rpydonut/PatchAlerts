from util import loader
from wrappers.update import Update
from games.base_class import Game


class RainbowSix(Game):
	def __init__(self):
		super().__init__('Rainbow Six Siege', homepage='https://rainbow6.ubisoft.com/siege/en-us/')

	def scan(self):
		data = loader.json("https://prod-tridionservice.ubisoft.com/live/v1/News/Latest?pageSize=6&pageIndex=0"
							"&language=en-US&templateId=tcm%3A152-76778-32&detailPageId=tcm%3A150-194572-64"
							"&keywordList=233416&useSeoFriendlyUrl=true")['items']  # Returns XML
		for p in data:
			soup = loader.direct_soup(p['Content'])
			_img = soup.find('img')['src']
			_title = soup.find('h3').text
			_desc = soup.find('strong').text
			_url = 'https://rainbow6.ubisoft.com/' + soup.find('a')['href']
			yield Update(game=self, update_name=_title, post_url=_url, desc=_desc, color='#333740', image=_img)


if __name__ == "__main__":
	lol = RainbowSix()
	for u in lol.scan():
		print(u)
