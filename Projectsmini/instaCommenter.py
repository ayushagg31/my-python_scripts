# Python bot for logging in and commenting on Instagram Post.
# Tech Used: Selenium 

# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def get_comment_input(browser):
    comment_input = browser.find_elements_by_xpath(
        '//textarea[@placeholder = "Add a comment…"]')
    if len(comment_input) <= 0:
        comment_input = browser.find_elements_by_xpath(
            '//input[@placeholder = "Add a comment…"]')
    return comment_input 

def open_comment_section(browser):
    missing_comment_elem_warning = (
        '--> Warning: Comment Button Not Found:'
        ' May cause issues with browser windows of smaller widths')
    comment_elem = browser.find_elements_by_xpath(
        "//a[@role='button']/span[text()='Comment']/..")
    if len(comment_elem) > 0:
        try:
            browser.execute_script(
                "arguments[0].click();", comment_elem[0])
        except WebDriverException:
            print(missing_comment_elem_warning)
    else:
        print(missing_comment_elem_warning)


browser = webdriver.Chrome(############) 	# add the path of your chrome web driver
browser.get('https://www.instagram.com/accounts/login/')
time.sleep(2)
username = browser.find_element_by_xpath('//input[@name="username"]')
username.send_keys('###########')	#username 
password = browser.find_element_by_xpath('//input[@name="password"]')
password.send_keys('############')	# password
logIn = browser.find_element_by_css_selector('._qv64e')
logIn.click()
time.sleep(5)
count=0
L = ['asmm','eppic','wonderland','woooow','cooool','wonderful','kepitup','good','perfect click','beaches']
while count < 10:
	browser.get("https://www.instagram.com/p/BeFXzKjDPwM/?taken-by=dm_ur_creativity");	# Sample post link
	browser.execute_script("window.scrollTo(0, 800)") 
	open_comment_section(browser)
	comment_input = get_comment_input(browser)
	if len(comment_input) > 0:
		comment_input[0].clear()
		comment_input = get_comment_input(browser)
		browser.execute_script("arguments[0].value = '" + L[count] + " ';", comment_input[0])
		comment_input[0].send_keys("\b")
		comment_input = get_comment_input(browser)
		comment_input[0].submit()
		count = count+1
		time.sleep(20)
#comm.clear()
#comm.send_keys("and some", Keys.ENTER);
#comment.send_keys(Keys.ENTER)
#browser.quit()
