''' This script takes a username and password from the user and opens gmail in firefox.
	It then logins to gmail using the above credentials, and sends a test mail to a user
	specified mail id. '''


import getpass
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



def login(web_browser, wait_object):
	user_name = raw_input("Enter username: ")
	password = getpass.getpass('Enter password: ')
	
	#enter username
	unameElem = browser.find_element_by_id('Email')
	unameElem.send_keys(user_name)
	unameElem.submit()
	wait.until(ec.presence_of_element_located((By.ID, 'Passwd' )))

	#enter password
	passElem = browser.find_element_by_id('Passwd')
	passElem.send_keys(password)
	passElem.submit()

def compose(web_browser, wait_object):
	#find and click compose
	wait.until(ec.element_to_be_clickable((By.XPATH, "//div[text()='COMPOSE']" )))
	compose = browser.find_element_by_xpath("//div[text()='COMPOSE']")
	compose.click()

	#change canvas - unnecessary
	#enter recipient mail id
	wait.until(ec.element_to_be_clickable((By.XPATH, "//textarea[@name='to']" )))
	toElem = browser.find_element_by_xpath("//textarea[@name='to']")
	to = raw_input('Enter recipient: ')
	toElem.send_keys(to)

	#enter subject
	subjectElem = browser.find_element_by_xpath("//input[@name='subjectbox']")
	subjectElem.send_keys("Test mail")
	
	#enter body
	bodyElem = browser.find_element_by_xpath("//div[@aria-label='Message Body']")
	bodyElem.send_keys("Message successfully constructed. Hope you receive this.")

	#send
	sendElem = browser.find_element_by_xpath("//div[text()='Send']")
	sendElem.click()


try:
	#open page
	browser = webdriver.Firefox()
	browser.get('https://gmail.com')
	wait = WebDriverWait(browser, 100)

	login(browser, wait)
	compose(browser, wait)

except Exception as e:
	print e

