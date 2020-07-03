# Python script for extracting data related to top query result on Kaggle website and save it in a csv file. This script was created as a part of web project.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
fields = ['Name','Location','Pagelink','LinkedIn Id','Current_Rank','Highest_Rank']	
# csv filename = kaggle_records.csv
filename = "kaggle_records.csv"
csvfile = open(filename,'w')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(fields)
# Chrome Webdriver location in your system
browser = webdriver.Chrome("/home/gozmit/Downloads/chromedriver") 
browser.get('https://www.kaggle.com/')
row = []
try:
	for i in range(1,6):
		del row[:]
		namesearch=browser.find_element_by_class_name('quick-search__search-box')
		namesearch.clear()
		# search key Ayush
		namesearch.send_keys('Ayush')	# search keyword
		time.sleep(10) #adjust it accrding to the net speed
		j=i
		while j>0:
			namesearch.send_keys(Keys.DOWN)
			j = j-1
		namesearch.send_keys(Keys.ENTER)
		name=browser.find_element_by_class_name('profile__head-display-name')
		row.append(name.text)
		location = browser.find_element_by_class_name('profile__user-location')
		row.append(location.text)
		row.append(browser.current_url)
		try:
			profile = browser.find_element_by_xpath('//li[2]/a[@rel="nofollow"]')
			row.append(profile.get_attribute('href'))
		except:
			row.append("Not Provided")
		try:
			curr_rank = browser.find_element_by_xpath('//a[1][@href="/rankings?group=competitions"]/div/div[2]')
			max_rank = browser.find_element_by_xpath('//a[2][@href="/rankings?group=competitions"]/div/div[2]')
			row.append(curr_rank.text)
			row.append(max_rank.text)
		except:
			row.append("Unranked")
			row.append("Unranked")
		csvwriter.writerow(row)
		#print(profile.text)
	browser.quit()
except:
	print("Code needs updation")
