#Opens the first five google search results in browser for a search query specified via command line

import requests, bs4, sys, webbrowser

print('googling for you....')

#Open url specified in command line
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#retrieve top search results
soup = bs4.BeautifulSoup(res.text)
print('\n',soup.prettify(),'\n')
print type(soup)
#open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open_new('http://google.com' + linkElems[i].get('href'), )


