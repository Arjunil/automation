#play 2048 with a keystroke sequence of up, right, down, left


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048')
htmlElem = browser.find_element_by_tag_name('html')
while(1):
	htmlElem.send_keys(Keys.UP)
	htmlElem.send_keys(Keys.RIGHT)
	htmlElem.send_keys(Keys.DOWN)
	htmlElem.send_keys(Keys.LEFT)
	try:
		game_over = browser.find_element_by_class_name('game-over')
	except Exception as e:
		#if exception raised
		continue
	else: 
		break

