from bs4 import BeautifulSoup
html_doc = """<html>
	
	<head><title>Doc</title></head>
	<body>
		<p>Hello this is a paragraph</p>
		<a href="#" id="one"<link1></a>
		<a href="#" id="two"<link2></a>
	</body>


</html>"""

soup = BeautifulSoup(html_doc,"html.parser")
print(soup)

print "---"*10
print soup.title.text
print "---"*10
print soup.get_text()	#print soup.text
print "---"*10
print "Find links "

for i in soup.find_all('a'):
	print i.get('href')