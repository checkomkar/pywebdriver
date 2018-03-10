from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from itertools import repeat
from selenium.common.exceptions import NoSuchElementException
import random
import time
from flask import Flask
from flask import jsonify
from flask import request



time.sleep(3)

like_counter = 0
num_of_rounds = 0
MAX_LIKES = 1500
users = ["adilmahfud_", 'travelandleisure', 'travelchannel', 'natgeotravel']
# tags = ['travelphotography', 'photography', 'summer', 'summerbody',  'instagood', 'babesofinstagram']
tags = ["nature", "bitemykitchen", "PleaseForgiveMe", "sky", "sun", "summer", "beach", "beautiful", 
			"pretty", "sunset", "sunrise", "blue", "flowers", "night", "tree", "twilight", "clouds", 
			"beauty", "light", "cloudporn", "photooftheday", "love", "green", "skylovers", "dusk", "weather", 
			"day", "red", "mothernature", "models", "babes", "travel", "travelphotography", "travelchannel", "travelandleisure"]
comments = ['Wow! O.O (y)', 'Such splendid.', 'Overly alluring shot =)', 
			'This is revolutionary work =)', 'Incredible work you have here.', 'Very Nice :) love it', 
			'Awesome! Keep em coming!', 'Magnificent. So amazing.', 'Just cool!', 'Cool shot.',
			'It\'s excellent not just good!', 
			'Just Love it!', 'Super like! O.o']


app = Flask(__name__)

@app.route("/autolikecomment", methods=['GET', 'POST'])
def autolikecomment():
	if request.method == 'GET':
		options = webdriver.ChromeOptions()
		# options.add_argument('headless')
		browser = webdriver.Chrome(chrome_options=options)
		browser.get('https://www.instagram.com/accounts/login/')
		#assert 'Yahoo!' in browser.title
		time.sleep(3)
		username = browser.find_element_by_name('username')  # Find the search box
		username.send_keys('stra.tus')
		password = browser.find_element_by_name('password')
		password.send_keys('enter_sandy3K' + Keys.ENTER)
		time.sleep(5)
		tagsCount = 0
		likesCount = 0
		random.shuffle(tags)
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
					if reps % 6 == 0:
						print('In mod')
						try:		
							element = browser.find_element_by_xpath("//*[@class='_8scx2 coreSpriteHeartOpen']")
							if element is not None:
								browser.find_element_by_class_name('_bilrf').clear()
								browser.find_element_by_class_name('_bilrf').send_keys(random.choice(comments) + Keys.ENTER)
								time.sleep(2)
						except NoSuchElementException:
							nxtArrow.click()
							time.sleep(5)
					
					try:			    
						likeelement = browser.find_element_by_xpath("//*[@class='_8scx2 coreSpriteHeartOpen']")
						likeelement.click()
						likesCount += likesCount			
						time.sleep(5)
					except NoSuchElementException:
						nxtArrow.click()
		    			time.sleep(5)
				except NoSuchElementException:
					break	
			tagsCount += tagsCount	
			time.sleep(10)

		browser.quit()
		return jsonify({"success": True, "likeCount": likesCount, "tagsCount": tagsCount})
    


if __name__ == "__main__":
	app.run()


#browser.quit()


