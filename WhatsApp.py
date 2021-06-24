#importing all the necessary libaries
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Chrome('/Users/dell/Downloads/chromedriver')
browser.get('https://web.whatsapp.com/')
wait = WebDriverWait(browser, 600)
#Sending a message to a single contact on WhatsApp
target = '"Apna"' #target user
string = "Message by python!" #target msg
x_arg = ' //span[contains(@title, ' + target +')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()
 
input_box = browser.find_element_by_class_name('_2A8P4')

for i in range(20):#loops runs for 100 times
    input_box.send_keys(string + Keys.ENTER)

#Sending Image Attachment 
file_path = "C:/Users/dell/OneDrive/Desktop/PHOTUU/github avatar.png"#file path
from time import sleep#sending image to whatsapp
attachment_section = browser.find_element_by_xpath('//div[@title = "Attach"]')
attachment_section.click()

image_box = browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(file_path)

browser.implicitly_wait(40)

send_button = browser.find_element_by_xpath('//span[@data-icon="send"]')
send_button.click()
#sending messages to multiple contacts

user_name_list = ['"Contact-1"','"Contact-2"','"Contact-3"'] #target contacts
browser.implicitly_wait(40)

for user_name in user_name_list:
    string = "Good Morning, Hope you are doing well! This message is sent by an automated bot, kindly ignore it." #target msg
    x_arg = ' //span[contains(@title, ' + user_name +')]'
    user_name = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
    user_name.click()
    input_box = browser.find_element_by_class_name('_2A8P4')

    for i in range(1):#loops runs for 1 times
        input_box.send_keys(string + Keys.ENTER)