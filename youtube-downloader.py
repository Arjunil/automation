import requests
from bs4 import BeautifulSoup
from subprocess import call

file_name = 'my_song_list.txt'

def get_song_names(file):
	names = []
	with open(file,'r') as f:
		for line in f :
			names.append(line)
	return names

song_names = get_song_names(file_name)

base_url = 'https://www.youtube.com/results?search_query='
for song in song_names :
	url = base_url + song
	response = requests.get(url)
	if response.status_code == 200 :
	
		soup = BeautifulSoup(response.text)
		for link in soup.find_all('a'):
			href = link.get('href')
			#print(href)
			if 'watch' in href: # can be optimised
				print(href)
				download_url = 'https://www.youtube.com' + href
				#edit for format change - currently 140 implies .m4a format
				call(['youtube-dl',download_url, '-f', '140'])
				break


