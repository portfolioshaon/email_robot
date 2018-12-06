#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,StaleElementReferenceException,WebDriverException,NoSuchElementException

import urllib.request,cv2,os,os.path,time,pickle,re

def read_file(filename):
	import codecs
	with codecs.open(filename, "r", encoding="utf-8") as file_reader:
		lines = file_reader.readlines()
	return lines

def get_credential(filename):
	file = read_file(filename)
	string = ''.join(file)
	return eval(string)

configs = get_credential('../config.py')
drivers_folder = '../browsers/'
chrome_name = 'chromedriver.exe'
browser_url = drivers_folder+chrome_name

def robist_mail(browser):
	browser.get(configs['gatoremail_home_url'])
	browser.find_element_by_link_text("Webmail").click()
	browser.find_element_by_id("user").send_keys(configs['gator_email_shaon'])
	browser.find_element_by_id("pass").send_keys(configs['gator_emailpass_shaon'])
	browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password'])[1]/following::button[1]").click()


	while True:
		if 'cpsess' in browser.current_url:
			break
		else:
			time.sleep(1)

	message_url = '/3rdparty/roundcube/?_task=mail&_action=compose'
	curl = browser.current_url.split('/')
	count = 0
	for c in curl:
		count = count + 1
		if "cpsess" in c:
			break

	curl = '/'.join(curl[0:count]) + message_url
	browser.get(curl)
	browser.find_element_by_id("_to").clear()
	browser.find_element_by_id("_to").send_keys(recepient)
	browser.find_element_by_id("compose-subject").clear()
	browser.find_element_by_id("compose-subject").send_keys(subject)
	browser.find_element_by_id("composebody").clear()
	browser.find_element_by_id("composebody").send_keys(body)
	browser.find_element_by_id("rcmbtn107").click()



if __name__ == "__main__":
	recepient = "example@example.com"
	subject = "Test Email"
	body = "This is a test"
	browser = webdriver.Chrome(browser_url)
	robist_mail(browser)