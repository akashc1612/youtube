from selenium import webdriver
from selenium.webdriver.common.keys import *
a = input("please enter the name of the song you want to play:")
driver = webdriver.Chrome(executable_path="C:/Users/path/to/chromedriver.exe")
driver.get("https://www.youtube.com")
elem = driver.find_element_by_name("search_query")
elem.clear()
elem.send_keys(a)
elem.send_keys(Keys.RETURN)
driver.find_element_by_id("dismissable").click()
