#importing all the necessary libaries
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome('/Users/dell/Downloads/chromedriver')
browser.get('https://web.whatsapp.com/')
wait = WebDriverWait(browser, 600)

target = '"Apna"' #target user
string = "Message by python!" #target msg
x_arg = ' //span[contains(@title, ' + target +')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()
 
input_box = browser.find_element_by_class_name('_2A8P4')

for i in range(20):#loops runs for 100 times
    input_box.send_keys(string + Keys.ENTER)