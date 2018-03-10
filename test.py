from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from itertools import repeat
from selenium.common.exceptions import NoSuchElementException
import random
import time

options = webdriver.ChromeOptions()
# options.add_argument('headless')
browser = webdriver.Chrome(chrome_options=options)

time.sleep(3)
browser.get('https://www.instagram.com/accounts/login/')
#assert 'Yahoo!' in browser.title
time.sleep(3)

like_counter = 0
num_of_rounds = 0
MAX_LIKES = 1500
users = ["adilmahfud_", 'travelandleisure', 'travelchannel', 'natgeotravel']
tags = ['travelphotography', 'photography', 'summer', 'summerbody',  'instagood', 'babesofinstagram']
comments = ['Wow! O.O (y)', 'Very Nice :) love it', 'Awesome! Keep em coming!', 'Just Love it!', 'Super like! O.o']

username = browser.find_element_by_name('username')  # Find the search box
username.send_keys('stra.tus')
password = browser.find_element_by_name('password')
password.send_keys('enter_sandy3K' + Keys.ENTER)
time.sleep(5)
#browser.quit()


for val in tags:
	browser.get("https://www.instagram.com/explore/tags/%s/?hl=en" %val) 
	time.sleep(2)
	#click first image
	browser.find_element_by_xpath("//*[@class='_mck9w _gvoze _tn0ps']").click()
	#browser.div(:class => '').click
	reps = 0
	time.sleep(3)
	for i in repeat(0,150):		
		print (i)
		reps += reps
		try:
			nxtArrow = browser.find_element_by_xpath("//*[@class='_3a693 coreSpriteRightPaginationArrow']")	
			if reps % 5 == 0:
				print('In mod')
				try:		
					element = browser.find_element_by_xpath("//*[@class='_8scx2 coreSpriteHeartOpen']")
					if element is not None:
						browser.find_element_by_class_name('_bilrf').clear()
						browser.find_element_by_class_name('_bilrf').send_keys(random.choice(comments) + Keys.ENTER)
						time.sleep(2)
				except NoSuchElementException:
					nxtArrow.click()
				
			
			try:			    
				likeelement = browser.find_element_by_xpath("//*[@class='_8scx2 coreSpriteHeartOpen']")
				likeelement.click()				
				time.sleep(5)
			except NoSuchElementException:
				nxtArrow.click()
    	
		except NoSuchElementException:
			break	
		
	time.sleep(10)

browser.quit()