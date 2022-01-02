import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
time.sleep(5)

driver.get("http://127.0.0.1:8000/contact.html")
time.sleep(5)

first_name = driver.find_elements("//input[@id='fname']")
first_name.send_keys("qwerty")
last_name = driver.find_elements("//input[@id='lname']")
last_name.send_keys("qwerty")
email = driver.find_elements("//input[@id='email']")
email.send_keys("fake@gmail.com")
subject = driver.find_elements("//input[@id='subject']")
email.send_keys("subject")
message = driver.find_elements("//textarea[@id='message']")
message.send_keys("message")

submit_button = driver.find_elements("//input[@type='submit']")
submit_button.click()
time.sleep(5)

driver.quit()

