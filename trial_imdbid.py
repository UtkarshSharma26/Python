import urllib2,json
from bs4 import BeautifulSoup as bs

f="http://www.imdb.com/title/tt5956100/?ref_=india_t_glfull"

def imdb_id():
	data = urllib2.urlopen(f).read()
	soup=bs(data)

	for i in soup.find_all('div',attrs={'class':'credit_summary_item'}):
		print i


imdb_id()
